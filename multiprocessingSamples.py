import api_nyt as nyt
import api_wikipedia as wiki
import manage_articles as mng
import statistics
import datetime
import pickle
import timeseries
import TextPreprocessing as txt
from datetime import date
import graphics
import matplotlib.pyplot as plt
import matching
import time
import word as wpy
import random
import numpy
import copy
from copy import deepcopy
import logging
import multiprocessing as mp

log_starttime = datetime.datetime.now()
logging.basicConfig(format='%(asctime)s [%(levelname)s] - %(message)s', datefmt='%d-%m-%y %H:%M:%S', level=logging.DEBUG)

mananger = mp.Manager()
output = mananger.Queue()

def single_run_partA(pid, articles):
    '''
    First part of a single run of a single process: Stops after interestingness was computed.

    '''
    logging.info("Starting PID {}".format(pid))
    if pid > 0:
        # create random sample and compute correlation
        articles = mng.shuffle_publicationdates(articles)
    logging.debug("PID {}: A".format(pid))
    #Get a dict of dicts for each calendar week with word frequencies from getWordCounts
    wordCounts = mng.getWordCounts(articles)
    #List of distinct words 
    distinctWords = mng.getDistinctWords(wordCounts)
    logging.debug("PID {}: B".format(pid))
    #List of lists of tuples containing weekly word frequency
    countsPerWeek = []
    for w in distinctWords:
        countsPerWeek.append((w,mng.getCountPerWeek(wordCounts,w)))
    logging.debug("PID {}: C".format(pid))
    #Create list of word objects for each keyword
    words = []
    for c in countsPerWeek:
        words.append(wpy.Word(c[0],ts_articles=timeseries.Timeseries(c[1])))
    logging.debug("PID {}: D".format(pid))
    interestingWords = mng.filter_interestingness(articles, 10, 5)
    keywords = []
    for k in interestingWords:
        keywords.append(k)
    logging.debug("PID {}: E".format(pid))
    output.put([pid,keywords,words])
    
def single_run_partB(pid, m, words):
    '''
    Second part of a single run of a single process: Starts after matching is done for all processes and computes correlation.

    '''
    logging.debug("PID {}: G".format(pid))
    words_analyze = [x for x in words if x.wikipediaSite != ""]
    logging.debug("PID {}: H".format(pid))
    #Drop all timepoints which are not contained in both article and wikipedia timeseries
    corr = []
    for w in words_analyze:
        w_timepointsordered = copy.deepcopy(w)
        w_timepointsordered.ts_articles.timepoints = sorted(w_timepointsordered.ts_articles.timepoints, key=lambda x: x.date, reverse=False)

        ts_a, ts_w = timeseries.alignTimeseries(w_timepointsordered.ts_articles,w_timepointsordered.ts_wiki)
        if len(ts_w.getCounts())<2 or len(ts_a.getCounts())<2:
            words_analyze.remove(w)
        else:
            corr.append(statistics.getCorrelation(ts_a.getCounts(),ts_w.getCounts()))
    logging.debug("PID {}: I".format(pid))
    output.put([pid,numpy.mean(corr)])
    logging.info("Finished PID {}".format(pid))

def run(n):
    '''
    Main function which starts and collects all processes. Matching is a critical section due to API calls and gets computed sequentially here.

    '''
    logging.info("Loading initial data ...")
    # Load all articles from 2019
    articles_original = mng.load_articles("nyt2019.json")
    logging.info("Done.")

    logging.info("Starting ...")
    processes = [mp.Process(target=single_run_partA, args=(pid, deepcopy(articles_original))) for pid in range(n+1)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    resultsA = [output.get() for p in processes]
    logging.info("Done with part A.")
    # ---------------------------------------- START OF CRITICAL SECTION ----------------------------------------
    m = {}
    res = {}
    logging.info("Matching...")
    for el in resultsA:
        m[el[0]] = matching.groupmatch(el[1], articles_original)
        logging.debug("Done with matching for PID {}".format(el[0]))
        for key in m[el[0]].keys():
            #Following line from 
            #https://stackoverflow.com/questions/7125467/find-object-in-list-that-has-attribute-equal-to-some-value-that-meets-any-condi
            try:
                word = next((x for x in el[2] if x.keyword == key), None)
                query = m[el[0]][key]['query']
                page = m[el[0]][key]['link'][1]
                wiki_counts = wiki.get_counts(page, word.ts_articles.getStartDate(), word.ts_articles.getEndDate(),"en")
                if wiki_counts is not None:
                    #If wikipedia timeseries exists
                    word.coocKeywords = query
                    word.wikipediaSite = page
                    word.ts_wiki = timeseries.parseWikipediaCounts(wiki_counts)
            except:
                print("ERROR: Key is invalid")
        res[el[0]] = el[2]
    logging.info("Done with matching.")
    # ---------------------------------------- END OF CRITICAL SECTION ----------------------------------------
    processes = [mp.Process(target=single_run_partB, args=(pid, deepcopy(m[pid]), deepcopy(res[pid]))) for pid in range(n+1)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    resultsB = [output.get() for p in processes]
    logging.info("Done with part B.")
    random_collection = []
    for el in resultsB:
        if len(el) == 2:
            if el[0] == 0:
                print("Mean correlation in original data: {}".format(el[1]))
            else:
                random_collection.append(el[1])
    print("Mean correlation in {} random samples: {}".format(n, statistics.mean_confidence_interval(random_collection)))
    print("Correlation of each sample:")
    print(random_collection)


run(1000)

log_endtime = datetime.datetime.now()
log_runtime = (log_endtime - log_starttime)
logging.info("Total runtime: " + str(log_runtime))