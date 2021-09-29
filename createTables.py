import logging
import manage_articles as mng
import datetime
from datetime import date, timedelta
import timeseries
import word as wpy
import json
import matching
import api_wikipedia as wiki
import multiprocessing as mp


def createYearlyDatabase(path_source, path_result, year):
    """
    Creates a database at ``path_results`` of world news articles for a given ``year`` using data from ``path_source``.

    Notes
    -----
    1.) Note that this function discards all items, which do not belong to the world news article section.
    2.) Works with NYT and TheGuardian data.

    Parameters
    ----------
    path_source : str
        Path on local machine where article database is located.
    path_result : str
        Path on local machine where resulting article dataset should be stored.
    year : int
        Year of publication of targeted articles (filter parameter).
    

    Returns
    -------
    dict
        Dict of article data in JSON format. 

    """
    data = mng.load_articles(path_source)
    if "guardian" in path_source.lower():
        data = mng.filter_articles(data, {"document_type": ["article"], "section_name": ["World news"]}, start=date(year,1,1), end=date(year,12,31))
    else:
        data = mng.filter_articles(data, {"document_type": ["article"], "type_of_material": ["News"], "section_name": ["World"]}, start=date(year,1,1), end=date(year,12,31))
    mng.store_articles(data, path_result)

def compute_topKeywordsTable(path_source, path_result, n=50):
    """
    Creates a Markdown table at ``path_results`` with the ``n`` most frequent (top) keywords of the database at ``path_source``. 

    Parameters
    ----------
    path_source : str
        Path on local machine where article database is located.
    path_result : str
        Path on local machine where resulting Markdown table should be stored.
    n : int
        Number of top keywords in the table (default is 50).
    
    Returns
    -------
    None 

    """
    articles = mng.load_articles(path_source)
    # Get a dict of dicts for each calendar week with word frequencies from getWordCounts
    wordCounts = mng.getWordCounts(articles)
    # List of distinct words 
    distinctWords = mng.getDistinctWords(wordCounts)
    # List of lists of tuples containing weekly word frequency
    countsPerWeek = []
    for w in distinctWords:
        countsPerWeek.append((w,mng.getCountPerWeek(wordCounts,w)))
    # Create list of word objects for each keyword
    words = []
    for c in countsPerWeek:
        yearCount = 0
        for el in c[1]:
            yearCount += el[1]
        words.append([c[0], yearCount])
    # Compute top keywords
    ts_sorted = sorted(words, key=lambda x: x[1], reverse=True)
    keywords = []
    for i in range(0,min(n,len(ts_sorted))):
        keywords.append(ts_sorted[i][0])
    m = matching.groupmatch(keywords, articles)
    writer = open(path_result,'a',encoding="utf-8")
    writer.write("| # | keyword | matching result (simple) | computed query (advanced)  | matching result (advanced) |")
    writer.write("\n|---|---|---|---|---|")
    for i in range(0,len(keywords)):
        simple = wiki.search_articles(ts_sorted[i][0], nmax=1)
        if len(simple) > 0 and len(m[ts_sorted[i][0]]["link"]) > 0:
            writer.write("\n| {}. | {} | {} | {} | {} |".format(i+1, ts_sorted[i][0], simple[1], m[ts_sorted[i][0]]["query"], m[ts_sorted[i][0]]["link"][1]))
        elif len(simple) > 0 and len(m[ts_sorted[i][0]]["link"]) == 0:
            writer.write("\n| {}. | {} | {} | {} | EMPTY MATCHING |".format(i+1, ts_sorted[i][0], simple[1], m[ts_sorted[i][0]]["query"]))
        elif len(simple) == 0 and len(m[ts_sorted[i][0]]["link"]) > 0:
            writer.write("\n| {}. | {} | EMPTY MATCHING | {} | {} |".format(i+1, ts_sorted[i][0], m[ts_sorted[i][0]]["query"], m[ts_sorted[i][0]]["link"][1]))
        elif len(simple) == 0 and len(m[ts_sorted[i][0]]["link"]) == 0:
            writer.write("\n| {}. | {} | EMPTY MATCHING | {} | EMPTY MATCHING |".format(i+1, ts_sorted[i][0], m[ts_sorted[i][0]]["query"]))
    writer.close()

def compute_mostInterestingKeywordsTable(path_source, path_result, min_weektotal=10, min_changerate=5):
    """
    Creates a Markdown table at ``path_results`` with the most interesting keywords of the database at ``path_source``. 

    Keywords must fulfill the following two conditions in at least one (and the same) week:
    1. Keyword was mentioned at least ``min_weektotal`` in that week.
    2. Keyword has a relative changerate of mentions of ``min_changerate`` compared to the previous week.

    Parameters
    ----------
    path_source : str
        Path on local machine where article database is located.
    path_result : str
        Path on local machine where resulting Markdown table should be stored.
    min_weektotal : int
        Minimum number of total mentions in at least one week (default is 10).
    min_changerate : int
        Minimum number for the relative changerate of mentions compared to the previous week (default is 5).
    
    Returns
    -------
    None 

    """
    articles = mng.load_articles(path_source)
    # Get a dict of dicts for each calendar week with word frequencies from getWordCounts
    wordCounts = mng.getWordCounts(articles)
    # List of distinct words 
    distinctWords = mng.getDistinctWords(wordCounts)
    # List of lists of tuples containing weekly word frequency
    countsPerWeek = []
    for w in distinctWords:
        countsPerWeek.append((w,mng.getCountPerWeek(wordCounts,w)))
    # Create list of word objects for each keyword
    words = []
    for c in countsPerWeek:
        words.append(wpy.Word(c[0],ts_articles=timeseries.Timeseries(c[1])))
    # Compute interestingness
    interestingWords = mng.filter_interestingness(articles, min_weektotal=min_weektotal, min_changerate=min_changerate)
    res = {}
    keywords = []
    for k in interestingWords:
        keywords.append(k)
        # Delete year but keep calendar week and round numbers:
        res[k] = {}
        for el in interestingWords[k]:
            res[k][el[1]] = [interestingWords[k][el][0], round(interestingWords[k][el][1],2)]
    m = matching.groupmatch(keywords, articles)
    writer = open(path_result,'a',encoding="utf-8")
    writer.write("|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |")
    writer.write("\n|---|---|---|---|---|")
    for i in range(0,len(keywords)):
        if len(m[keywords[i]]["link"]) > 0:
            writer.write("\n| {}. | {} | {} | {} | {} |".format(i+1, keywords[i], res[keywords[i]], m[keywords[i]]["query"], m[keywords[i]]["link"][1]).replace("{","").replace("}",""))
        else:
            writer.write("\n| {}. | {} | {} | {} | EMPTY MATCHING |".format(i+1, keywords[i], res[keywords[i]], m[keywords[i]]["query"]).replace("{","").replace("}",""))
    writer.close()


'''
# Create yearly database of world news articles for NYT and TheGuardian:
for year in range(2001,2021):
    createYearlyDatabase("/home/lmoldon/forschungspraktikum/nyt_reduced.json", "/home/lmoldon/forschungspraktikum/data/nyt{}.json".format(year), year)
    compute_topKeywordsTable("/home/lmoldon/forschungspraktikum/data/nyt{}.json".format(year), "/home/lmoldon/forschungspraktikum/results/nytTop{}.md".format(year))
    compute_mostInterestingKeywordsTable("/home/lmoldon/forschungspraktikum/data/nyt{}.json".format(year), "/home/lmoldon/forschungspraktikum/results/nytMostInteresting{}.md".format(year))
    createYearlyDatabase("/home/lmoldon/forschungspraktikum/theguardian_reduced.json", "/home/lmoldon/forschungspraktikum/theguardian{}.json".format(year), year)
    compute_topKeywordsTable("/home/lmoldon/forschungspraktikum/data/theguardian{}.json".format(year), "/home/lmoldon/forschungspraktikum/results/theguardianTop{}.md".format(year))
    compute_mostInterestingKeywordsTable("/home/lmoldon/forschungspraktikum/data/theguardian{}.json".format(year), "/home/lmoldon/forschungspraktikum/results/theguardianMostInteresting{}.md".format(year))
'''

'''
# WITH MULTIPROCESSING: Create yearly database of world news articles for NYT and TheGuardian:
def single_run(year, nyt):
    if nyt:
        createYearlyDatabase("/home/lmoldon/forschungspraktikum/nyt_reduced.json", "/home/lmoldon/forschungspraktikum/data/nyt{}.json".format(year), year)
        compute_topKeywordsTable("/home/lmoldon/forschungspraktikum/data/nyt{}.json".format(year), "/home/lmoldon/forschungspraktikum/results/nytTop{}.md".format(year))
        compute_mostInterestingKeywordsTable("/home/lmoldon/forschungspraktikum/data/nyt{}.json".format(year), "/home/lmoldon/forschungspraktikum/results/nytMostInteresting{}.md".format(year))
    else:
        createYearlyDatabase("/home/lmoldon/forschungspraktikum/theguardian_reduced.json", "/home/lmoldon/forschungspraktikum/data/theguardian{}.json".format(year), year)
        compute_topKeywordsTable("/home/lmoldon/forschungspraktikum/data/theguardian{}.json".format(year), "/home/lmoldon/forschungspraktikum/results/theguardianTop{}.md".format(year))
        compute_mostInterestingKeywordsTable("/home/lmoldon/forschungspraktikum/data/theguardian{}.json".format(year), "/home/lmoldon/forschungspraktikum/results/theguardianMostInteresting{}.md".format(year))

tasks = []
for year in range(2001,2021):
    for flag in range(0,2):
        tasks.append((year, flag))
processes = [mp.Process(target=single_run, args=(task[0], task[1])) for task in tasks]
for p in processes:
    p.start()
for p in processes:
    p.join()
'''