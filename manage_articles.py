import logging
import numpy as np
import json
import datetime
import random
import regex
import TextPreprocessing as txt
from collections import Counter
from itertools import combinations
import copy

def load_articles(path_data):
    """
    Loading article data.

    Parameters
    ----------
    path_data : str
        Path on local machine where article dataset is located.
    
    Returns
    -------
    dict
        Dict of article data in JSON format.

    """
    with open(path_data) as fp:
        articles = json.load(fp)
    return articles

def store_articles(articles, path_data):
    """
    Storing article data.

    Parameters
    ----------
    articles : dict
        Dict of articles in JSON format which should be stored.
    path_data : str
        Path on local machine where article dataset should be stored.
    
    Returns
    -------
    None

    """
    with open(path_data, "w") as fp:
        json.dump(articles, fp)

def get_article(articles, year, month, count, article_property):
    """
    Get the property value of a single article in given article data.

    Returns the value of the property ``article_property`` in the data ``articles`` with ID ``count`` which was published in ``month``/``year``. 

    Parameters
    ----------
    articles : dict
        Dict of articles in JSON format containing the target article.
    year : int
        Year of publication of target article.
    month : int
        Month of publication of target article.
    count : int
        ID of target article (each month starts with ID 1).
    article_property : str
        key name of the article property which should be returned.

    Returns
    -------
    str
        value of the property of the selected article.

    """
    return articles[str(year)][str(month)][count][article_property]

def filter_articles(articles, restrictions={}, start=None, end=None):
    """
    Filter article data with given restrictions.

    Returns the given article data with applied filter rules:
    - only articles, which have for each attribute in ``restrictions`` (key of dict) a match with one the values in the 
      corresponding list in ``restrictions`` (value of dict).
    - only articles, which have been published between on or after day ``start``.
    - only articles, which have been published between on or before day ``end``.

    Parameters
    ----------
    articles : dict
        Dict of news articles in JSON format.
    restrictions : dict
        Dict of restrictions with format {attribute_name: [attribute values which pass the filter and remain in data]} 
        (default is empty dict for no restriction).
    start : datetime.date
        First day of pageview statistic (default is None for no restriction).
    end : datetime.date
        Last day of pageview statistic (default is None for no restriction).

    Returns
    -------
    dict
        Dict of articles which passed the filter and fullfilled the restrictions.

    """
    result = {}
    for y in articles.keys():
        result[y] = {}
        for m in articles[y].keys():
            result[y][m] = {}
            for a in articles[y][m]:
                accept = True
                if start != None or end != None:
                    date = parse_pubdate(articles[y][m][a]["pub_date"])
                    if start != None:
                        if date < start:
                            accept = False
                    if end != None:
                        if date > end:
                            accept = False
                for restriction_attribute in restrictions:
                    if articles[y][m][a][restriction_attribute] not in restrictions[restriction_attribute]:
                        accept = False
                        break
                if accept:
                    result[y][m][a] = articles[y][m][a]
    return result

def get_attributes(articles, attribute):
    """
    Get all occuring values of a given ``attribute`` (no duplicates) in a given dataset of ``articles``.

    Parameters
    ----------
    articles : dict
        Dict of news articles in JSON format.
    attribute : str
        Selected attribute name (e.g. 'abstract').

    Returns
    -------
    set of str
        Set of all values for the given attribute.

    """
    attributes = set()
    for y in articles.keys():
        for m in articles[y].keys():
            for a in articles[y][m]:
                attributes.add(articles[y][m][a][attribute])
    return attributes

def count_attributes(articles, attribute):
    """
    Count all occuring values of a given ``attribute`` in a given dataset of ``articles``.

    Parameters
    ----------
    articles : dict
        Dict of news articles in JSON format.
    attribute : str
        Selected attribute name (e.g. 'pub_date').

    Returns
    -------
    dict
        Dict of all attribute values (key of dict) with their frequency (value of dict).

    """
    attributes = {}
    for y in articles.keys():
        for m in articles[y].keys():
            for a in articles[y][m]:
                val = articles[y][m][a][attribute]
                if val in attributes:
                    attributes[val] += 1
                else:
                    attributes[val] = 1
    return {k: v for k, v in sorted(attributes.items(), key=lambda item: item[1], reverse=True)}

def generate_subsample(articles, amount):
    """
    Create a random subset of size ``amount`` of a given dataset of ``articles``.

    Parameters
    ----------
    articles : dict
        Dict of news articles in JSON format.
    amount : int
        Size of the subset.

    Returns
    -------
    dict
        Subsample of article data (dict of articles). Article keys change to ``year``-``month``-``ID`` and an optional empty
        entry for the ground truth label gets added (for labeling data, see README.md).

    """
    result = {}
    while len(result) != amount:
        try:
            y = random.choice(list(articles.keys()))
            m = random.choice(list(articles[y].keys()))
            a = random.choice(list(articles[y][m].keys()))
            result[y+"-"+m+"-"+a] = articles[y][m][a]
            result[y+"-"+m+"-"+a]["ground_truth"] = [""]
        except:
            pass
    return result

def get_articles_as_list(articles):
    """
    Get a 'flat' list of all ``articles``.

    Parameters
    ----------
    articles : dict
        Dict of news articles in JSON format.

    Returns
    -------
    list
        List of articles (each article in dict format).

    """
    result = []
    for y in articles.keys():
        for m in articles[y].keys():
            for a in articles[y][m]:
                result.append(articles[y][m][a])
    return result

def getCalendarWeek(dat):
    """
    Get calendar week of timestamp.

    Parameters
    ----------
    dat : str
        Timestamp with NYT or TheGuardian format.

    Returns
    -------
    int
        Calendar week of timestamp.

    """
    match = regex.match(r"\d{4}-\d{2}-\d{2}", dat).group(0)
    return datetime.datetime.strptime(match,'%Y-%m-%d').isocalendar()[1]
    
def getYear(dat):
    """
    Get year of timestamp.

    Parameters
    ----------
    dat : str
        Timestamp with NYT or TheGuardian format.

    Returns
    -------
    int
        Year of timestamp.

    """
    match = regex.match(r"\d{4}-\d{2}-\d{2}", dat).group(0)
    return datetime.datetime.strptime(match,'%Y-%m-%d').isocalendar()[0]

def getWordCounts(articles, useAbstract=True):
    """
    Get for each calendar week the word frequencies of all occuring words in the headlines 
    (and optionally also abstracts) in the given dataset of ``articles``.

    Parameters
    ----------
    articles : dict
        Dict of news articles in JSON format.
    useAbstract : bool
        Specifies whether the abstract should also be used - only available for NYT (default is True).

    Returns
    -------
    dict
        Dict of dicts for each calendar week with word frequencies.

    """
    result = {}
    articles = get_articles_as_list(articles)
    for a in articles:
        key = (getYear(a['pub_date']),getCalendarWeek(a['pub_date']))
        if key not in result:
            result[key] = {}
        for w in txt.parseSentence(a['headline']):
            if w not in result[key]:
                result[key][w] = 1
            else: 
                result[key][w] += 1 
        if useAbstract and "abstract" in a:
            for w in txt.parseSentence(a['abstract']):
                if w not in result[key]:
                    result[key][w] = 1
                else: 
                    result[key][w] += 1 
    return result

def getTopWordsForWeek(words, n=10):
    """
    Get for each calendar week the ``n`` most frequent words in dict ``words``.

    Parameters
    ----------
    words : dict
        Dict of dicts for each calendar week with word frequencies (obtained from ``getWordCounts``).
    n : int
        Number of results per calendar week (top ``n`` descending).

    Returns
    -------
    list
        List of tupels with format: (week, {``n`` top words})

    """
    result = []
    for k in words.keys():
        result.append((k,sorted(words[k].items(), key=lambda x:x[1],reverse=True)[:n]))
    return result
    

def getDistinctWords(words):
    """
    Get a 'flat' list of all distinct words in dict ``words``.

    Parameters
    ----------
    words : dict
        Dict of dicts for each calendar week with word frequencies (obtained from ``getWordCounts``).

    Returns
    -------
    list
        List of distinct words.

    """
    result = []
    for k in words.keys():
        for w in words[k].items():
            if w[0] not in result:
                result.append(w[0])
    return result

def getCountPerWeek(words, word):
    """
    Get word frequency of ``word`` for each calendar week in ``words``.

    Parameters
    ----------
    words : dict
        Dict of dicts for each calendar week with word frequencies (obtained from ``getWordCounts``).
    word : str
        Selected word.

    Returns
    -------
    list
        List of tuples containing weekly word frequency with format: (week, count)

    """
    weeks = []
    for w in words.keys():
        if word in words[w]:
            weeks.append((w,words[w][word]))
        else:
            weeks.append((w,0))
    return weeks

def get_cooccurrences(keyword, articles, start=None, end=None, useAbstract=True):
    """
    Get co-occurring words for single ``keyword``.

    Searches all words which occur together with ``keyword`` in headlines and abstracts for the given dataset of ``articles``.

    Notes
    -----
    1.) For multiple different keywords use ``get_group_cooccurrences`` for better runtime.
    2.) In contrast to ``restore_keyword``, here we do not consider the positional distance of a word to the keyword in the headline/abstract. 

    Parameters
    ----------
    keyword : str
        Keyword in ``articles``.
    articles : dict
        Dict of news articles in JSON format.
    start : datetime.date
        Search is limited to articles which were published on or after this day (defaut is None).
    end : datetime.date
        Search is limited to articles which were published on or before this day (defaut is None).
    useAbstract : bool
        Specifies whether the abstract should also be used - only available for NYT (default is True).

    Returns
    -------
    list
        Sorted (descending count) list of tuples with format: (co-occurring_keyword, count)

    """
    result = {}
    articles = get_articles_as_list(articles)
    for a in articles:
        match = True
        if "abstract" in a and useAbstract:
            content = txt.parseSentence(a["headline"] + " " + a["abstract"])
        else:
            content = txt.parseSentence(a["headline"])
        if keyword not in content:
            match = False
        if match and (start != None or end != None):
            date = parse_pubdate(a["pub_date"])
            if start != None:
                if date < start:
                    match = False
            if end != None:
                if date > end:
                    match = False
        if match:
            for cooccurrence in content:
                if cooccurrence != keyword:
                    if cooccurrence not in result:
                        result[cooccurrence] = 1
                    else:
                        result[cooccurrence] += 1
    return [(k, result[k]) for k in sorted(result, key=result.get, reverse=True)]

def get_group_cooccurrences(keywords, articles, starts=None, ends=None, useAbstract=True):
    """
    Get co-occurring words for multiple ``keywords``.

    Searches all words which occur together with words from ``keywords`` in headlines and abstracts for the given dataset of ``articles``.

    Notes
    -----
    In contrast to ``restore_keyword``, here we do not consider the positional distance of a word to the keyword in the headline/abstract. 

    Parameters
    ----------
    keywords : list
        List of keywords in ``articles``.
    articles : dict
        Dict of news articles in JSON format.
    starts : list of datetime.date
        Search is limited to articles which were published on or after this day depending on keyword (defaut is None).
    ends : list of datetime.date
        Search is limited to articles which were published on or before this day depending on keyword (defaut is None).
    useAbstract : bool
        Specifies whether the abstract should also be used - only available for NYT (default is True).

    Returns
    -------
    dict
        Dict containing for each keyword a sorted (descending count) list of tuples with format: (co-occurring_keyword, count)

    """
    result = {}
    for keyword in keywords:
        result[keyword] = {}
    articles = get_articles_as_list(articles)
    for a in articles:
        if "abstract" in a and useAbstract:
            content = txt.parseSentence(a["headline"] + " " + a["abstract"])
        else:
            content = txt.parseSentence(a["headline"])
        for keyword in keywords:
            match = True
            if keyword not in content:
                match = False
            if match and (starts != None or ends != None):
                date = parse_pubdate(a["pub_date"])
                if starts[keyword] != None:
                    if date < starts[keyword]:
                        match = False
                if ends[keyword] != None:
                    if date > ends[keyword]:
                        match = False
            if match:
                for cooccurrence in content:
                    if cooccurrence != keyword:
                        if cooccurrence not in result[keyword]:
                            result[keyword][cooccurrence] = 1
                        else:
                            result[keyword][cooccurrence] += 1
    for keyword in keywords:
        result[keyword] = [(k, result[keyword][k]) for k in sorted(result[keyword], key=result[keyword].get, reverse=True)]
    return result

def subsequence_counts(sequences, minLength=2, minCount=2):
    """
    Count all word-subsequences of ``sequences`` consisting of at least ``minLength`` words and occurring at least ``minCount`` times.

    Parameters
    ----------
    sequences : list
        List of lists, which represents lists of sentences (each element of a sentence-list is a word).
    minLength : int
        Minimum length (number of words) of the subsequence (defaut is 2).
    minCount : int
        Minimum amount of occurrences of the subsequence (defaut is 5).

    Returns
    -------
    list
        List of tupels with format: (subsequence, count)

    """
    # source for following single line of code: https://codereview.stackexchange.com/questions/108052/finding-most-common-contiguous-sub-lists-in-an-array-of-lists
    counts = Counter(seq[i:j] for seq in map(tuple, sequences) for i, j in combinations(range(len(seq) + 1), 2))
    result = []
    for el in counts:
        if len(el) >= minLength and counts[el] > minCount:
            result.append([el, counts[el]])
    return result

def restore_keyword(keyword, articles, start=None, end=None, searchrange=None, minLength=2, minCount=5, useAbstract=True):
    """
    Get subsequences of words which contain single ``keyword``.

    Searches all subsequences of words which contain the ``keyword`` in headlines and abstracts for the given dataset of ``articles``.

    Notes
    -----
    1.) In contrast to ``get_cooccurrences``, here we consider the positional distance of a word to the keyword in the headline/abstract.
    2.) Using ``searchrange`` increases the performance.

    Parameters
    ----------
    keyword : str
        Keyword in ``articles``.
    articles : dict
        Dict of news articles in JSON format.
    start : datetime.date
        Search is limited to articles which were published on or after this day (defaut is None).
    end : datetime.date
        Search is limited to articles which were published on or before this day (defaut is None).
    searchrange : int
        Only consider words within this maximum (symmetric) positional distance to the keyword in the headline/abstract (defaut is None).
    minLength : int
        Minimum length (number of words) of the subsequence (defaut is 2).
    minCount : int
        Minimum amount of occurrences of the subsequence (defaut is 5).
    useAbstract : bool
        Specifies whether the abstract should also be used - only available for NYT (default is True).

    Returns
    -------
    list
        Sorted (descending count) list of tuples with format: (word_sequence, count)

    """
    data = []
    articles = get_articles_as_list(articles)
    for a in articles:
        match = True
        if "abstract" in a and useAbstract:
            content = txt.parseSentence(a["headline"] + " " + a["abstract"])
        else:
            content = txt.parseSentence(a["headline"])
        if keyword not in content:
            match = False
        if match and (start != None or end != None):
            date = parse_pubdate(a["pub_date"])
            if start != None:
                if date < start:
                    match = False
            if end != None:
                if date > end:
                    match = False
        if match:
            if searchrange != None:
                for index in [i for i, v in enumerate(content) if v == keyword]:
                    data.append(content[max(index-searchrange-1,0):min(index+searchrange,len(content))])
            else:
                data.append(content)
    substring_counts = subsequence_counts(data, minLength=minLength, minCount=minCount)
    result = {}
    for el in substring_counts:
        if keyword in el[0]:
            result[" ".join(el[0])] = el[1]
    return [(k, result[k]) for k in sorted(result, key=result.get, reverse=True)]

def parse_pubdate(timestamp):
    """
    Convert a timestamp (string) of NYT/TheGuardian/common format to date object.

    Parameters
    ----------
    timestamp : str
        Timestamp to be converted.

    Returns
    -------
    datetime.date
        Resulting date object.

    """
    if len(timestamp) == 10:
        return datetime.datetime.strptime(timestamp, "%Y-%m-%d").date() # common day-only timestamp format
    elif timestamp.count("Z") == 1:
        return datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ").date() # theguardian timestamp format
    else:
        return datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S+%f").date() # nyt timestamp format

def shuffle_publicationdates(articles):
    """
    Get a copy of the articles with shuffled publication dates.

    Notes
    -----
    The function computes the distribution of publication dates in the given data and 
    then randomly draws a publication date for each article from the distribution.

    Parameters
    ----------
    articles : dict
        Dict of news articles in JSON format.

    Returns
    -------
    dict
        Same dict of articles, but with shuffled publication dates.

    """
    articles = copy.deepcopy(articles)
    distr = {}
    n = 0
    for y in articles.keys():
        for m in articles[y].keys():
            for a in articles[y][m]:
                date = str(parse_pubdate(articles[y][m][a]["pub_date"]))
                n += 1
                if date not in distr:
                    distr[date] = 1
                else:
                    distr[date] += 1
    x = [] # list of dates
    p = [] # probability = frequency of each date
    for day in distr:
        x.append(day)
        p.append(distr[day]/n)
    for y in articles.keys():
        for m in articles[y].keys():
            for a in articles[y][m]:
                articles[y][m][a]["pub_date"] = np.random.choice(x,p=p)
    return articles

def get_keywords(articles, useAbstract=True):
    """
    Get a set of all keywords which occur in the headlines (and optionally also abstracts) in ``articles``.

    Parameters
    ----------
    articles : dict
        Dict of news articles in JSON format.
    useAbstract : bool
        Specifies whether the abstract should also be used - only available for NYT (default is True).

    Returns
    -------
    set
        Set of keywords.

    """
    keywords = set()
    articles = get_articles_as_list(articles)
    for a in articles:
        for keyword in a["headline"]:
            keywords.add(keyword)
        if useAbstract and "abstract" in a:
            for keyword in a["abstract"]:
                keywords.add(keyword)
    return keywords

def get_keyword_changerate(articles, useAbstract=True):
    """
    Compute weekly changerates of keyword frequencies in ``articles``.

    Notes
    -----
    If a keyword occurs in a specific week but not in the week before, the changerate is set to ``float('inf')``.

    Parameters
    ----------
    articles : dict
        Dict of news articles in JSON format.
    useAbstract : bool
        Specifies whether the abstract should also be used - only available for NYT (default is True).

    Returns
    -------
    dict
        Dict of calendar weeks, contains all keywords as dict with their weekly total count [0] and changerate [1] (compared to previous week).

    """
    counts = getWordCounts(articles, useAbstract=useAbstract)
    keywords = get_keywords(articles, useAbstract=useAbstract)
    changerate = {}
    for week in counts:
        changerate[week] = {}
        for keyword in keywords:
            changerate[week][keyword] = [0, 0] # = [total, changerate from previous week]
    for week in counts:
        previousweek = None
        if (week[0], week[1]-1) in counts:
            previousweek = (week[0], week[1]-1)
        elif (week[0]-1, 52) in counts:
            previousweek = (week[0]-1, 52)
        elif (week[0]-1, 53) in counts:
            previousweek = (week[0]-1, 53)
        if previousweek != None:
            for keyword in counts[week]:
                if keyword not in counts[previousweek]:
                    changerate[week][keyword] = [counts[week][keyword], float('inf')]
                else:
                    changerate[week][keyword] = [counts[week][keyword], counts[week][keyword]/counts[previousweek][keyword]]
    return changerate

def filter_interestingness(articles, min_weektotal=5, min_changerate=2, useAbstract=True):
    """
    Get all keywords which occured at least ``min_weektotal`` in any week with a minimum changerate of ``min_changerate``.

    Notes
    -----
    Returned dict is sorted descending by the max changerate of each keyword.

    Parameters
    ----------
    articles : dict
        Dict of news articles in JSON format.
    min_weektotal : int
        Specifies the minimum total count within a week to be counted (default is 5).
    min_changerate : int
        Specifies the minimum changerate within a week compared to the previous week to be counted (default is 2).
    useAbstract : bool
        Specifies whether the abstract should also be used - only available for NYT (default is True).

    Returns
    -------
    dict
        Dict of keywords, contains all calendar weeks where restrictions are fulfilled with corresponding weekly total count [0] and changerate [1] (compared to previous week).

    """
    changerate = get_keyword_changerate(articles, useAbstract=useAbstract)
    result = {}
    rates = [] # only for sorting
    # filter:
    for week in changerate:
        for keyword in changerate[week]:
            if changerate[week][keyword][0] >= min_weektotal and changerate[week][keyword][1] >= min_changerate:
                if keyword not in result:
                    result[keyword] = {}
                result[keyword][week] = changerate[week][keyword]
                rates.append(changerate[week][keyword][1])
    # sort:
    rates = list(sorted(set(rates), reverse=True))
    result_sorted = {}
    for rate in rates:
        for keyword in result:
            if keyword not in result_sorted:
                maxrate = 0
                for week in result[keyword]:
                    maxrate = max(maxrate,result[keyword][week][1])
                if maxrate == rate:
                    result_sorted[keyword] = result[keyword]
    return result_sorted


#d_nyt = load_articles("/home/lmoldon/forschungspraktikum/nyt.json")
#d_theguardian = load_articles("/home/lmoldon/forschungspraktikum/theguardian.json")

#print(get_article(d_nyt, 2002, 2, 21, "headline"))

#print(count_attributes(d_nyt, "type_of_material"))
#print(count_attributes(d_theguardian, "document_type"))

#d_nyt_reduced = filter_articles(d_nyt, {"document_type": ["article"], "type_of_material": ["News"], "section_name": ["World"]})
#d_theguardian_reduced = filter_articles(d_theguardian, {"document_type": ["article"], "section_name": ["World news"]})
#store_articles(d_nyt_reduced, "/home/lmoldon/forschungspraktikum/nyt_reduced.json")
#store_articles(d_theguardian_reduced, "/home/lmoldon/forschungspraktikum/theguardian_reduced.json")

#d_nyt_ground_truth = generate_subsample(filter_articles(d_nyt, {"document_type": ["article"], "type_of_material": ["News"], "section_name": ["World"]}), 200)
#d_theguardian_ground_truth = generate_subsample(filter_articles(d_theguardian, {"document_type": ["article"], "section_name": ["World news"]}), 200)
#store_articles(d_nyt_ground_truth, "/home/lmoldon/forschungspraktikum/nyt_ground_truth.json")
#store_articles(d_theguardian_ground_truth, "/home/lmoldon/forschungspraktikum/theguardian_ground_truth.json")

#nyt2019 = load_articles("nyt2019.json")
#print(get_cooccurrences("trump", nyt2019))
#print(restore_keyword("trump", nyt2019))

#print(filter_interestingness(nyt2019, 10, 5))