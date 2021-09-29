import logging
import json
import datetime
from datetime import timedelta
import api_wikipedia as wiki
import manage_articles as mng
import time


def match(keyword, articles, restore_keyword=False, date=None, cooc_daterange=None, cooc_wordcount=2, nmax=1, timeout=10, useAbstract=True):
    """
    Match single keywords from the news with wikipedia articles using advanced methods.

    This matching alogrithm uses keyword co-occurrences which occur together with ``keyword`` in headlines and abstracts for the given dataset of ``articles``.
    Optionally it also searches all subsequences of words which contain the ``keyword``. Then it computes a final query from this information at sends it to the API.

    Notes
    -----
    1.) Do not make more than one api function call per second due to given request limits by wikipedia. 
    2.) For matching multiple keywords, use the function ``groupmatch`` instead for better performance over time.
    3.) This implementation is not deterministic, the wikipedia API returns different results within hours.
    4.) If optional parameter ``date`` gets used, only articles which already existed at ``date`` will be returned, which increases the runtime 
    in certain circumstances significantly. Make sure to use the parameter ``timeout`` in this case, to limit the runtime for a single query.
    5.) Using ``restore_keyword`` decreases performance significantly, but does not seem to improve the quality noticeably.

    Parameters
    ----------
    keyword : str
        Keyword in ``articles``.
    articles : dict
        Dict of news articles in JSON format.
    restore_keyword : bool
        Specifies whether keyword neighbors should additionally be searched (default is False, see ``restore_keyword`` function).
    date : datetime.date
        Results are limited to articles which already existed at ``date`` (default is None, see Notes).
    cooc_daterange : int
        Symmetric date range around ``date`` for searching co-occurring keywords (default is None: search in whole article data).
    cooc_wordcount : int
        Specifies how many most co-occurring keywords will be used for searchig related wiki articles (default is 2).
    nmax : int
        Specifies the maximum number of related wikipedia articles which should be returned (default is 1: only return best match).
    timeout : int
        Limits the runtime for this query to ``timeout`` seconds. When exceeding the threshold, intermediate results will be returned (default is 10).
    useAbstract : bool
        Specifies whether the abstract should also be used - only available for NYT (default is True).

    Returns
    -------
    dict
        Dict containing the computed advanced query for the API and the corresponding result. 

    """
    if cooc_daterange == None:
        cooc = mng.get_cooccurrences(keyword, articles, useAbstract=useAbstract)
        if restore_keyword:
            restored = mng.restore_keyword(keyword, articles)[0][0]
    else:
        start = date - timedelta(days=cooc_daterange)
        end = date + timedelta(days=cooc_daterange)
        cooc = mng.get_cooccurrences(keyword, articles, start=start, end=end, useAbstract=useAbstract)
        if restore_keyword:
            restored = mng.restore_keyword(keyword, articles, start=start, end=end, useAbstract=useAbstract)[0][0]
    cooc = cooc[:cooc_wordcount]
    if restore_keyword:
        query = set(restored.split())
        for el in cooc:
            query.add(el[0])
        query = " ".join(query)
    else:
        query = keyword
        for el in cooc:
            query += " " + el[0]
    matching = {
                "query": query,
                "link": wiki.search_articles(query, nmax=nmax, date=date, timeout=timeout)
    }

    return matching

def groupmatch(keywords, articles, dates=None, cooc_daterange=None, cooc_wordcount=2, nmax=1, timeout=10, useAbstract=True):
    """
    Match multiple different keywords from the news with wikipedia articles using advanced methods.

    This matching alogrithm uses keyword co-occurrences which occur together with ``keyword`` in headlines and abstracts for the given dataset of ``articles``.
    Then it computes a final query from this information at sends it to the API.

    Notes
    -----
    1.) This implementation is not deterministic, the wikipedia API returns different results within hours.
    2.) If optional parameter ``dates`` gets used, only articles which already existed at ``dates`` will be returned, which increases the runtime 
    in certain circumstances significantly. Make sure to use the parameter ``timeout`` in this case, to limit the runtime for a single query.

    Parameters
    ----------
    keywords : list of str
        List of keywords in ``articles``.
    articles : dict
        Dict of news articles in JSON format.
    dates : list of datetime.date
        Results are limited to articles which already existed at correspnding value of ``dates`` (default is None, see Notes).
    cooc_daterange : int
        Symmetric date range around ``date`` for searching co-occurring keywords (default is None: search in whole article data).
    cooc_wordcount : int
        Specifies how many most co-occurring keywords will be used for searchig related wiki articles (default is 2).
    nmax : int
        Specifies the maximum number of related wikipedia articles which should be returned (default is 1: only return best match).
    timeout : int
        Limits the runtime for this query to ``timeout`` seconds. When exceeding the threshold, intermediate results will be returned (default is 10).
    useAbstract : bool
        Specifies whether the abstract should also be used - only available for NYT (default is True).

    Returns
    -------
    dict
        Dict containing for each keyword the computed advanced query for the API and the corresponding result. 

    """
    matching = {}
    if dates != None and cooc_daterange != None:
        starts = {}
        ends = {}
        for keyword in keywords:
            date = dates[keywords.index(keyword)]
            start = date - timedelta(days=cooc_daterange)
            end = date + timedelta(days=cooc_daterange)
            starts[keyword] = start
            ends[keyword] = end
        coocs = mng.get_group_cooccurrences(keywords, articles, starts, ends, useAbstract)
    else:
        coocs = mng.get_group_cooccurrences(keywords, articles, useAbstract=useAbstract)
    for keyword in keywords:
        if dates != None and cooc_daterange != None:
            date = dates[keywords.index(keyword)]
        else:
            date = None
        matching[keyword] = {}
        cooc = coocs[keyword][:cooc_wordcount]
        query = keyword
        for el in cooc:
            query += " " + el[0]
        time.sleep(1)
        matching[keyword] = {
            "query": query, 
            "link": wiki.search_articles(query, nmax=nmax, date=date, timeout=timeout)
        }
    return matching

def groupmatch_old(keywords, articles, restore_keyword=False, dates=None, cooc_daterange=None, cooc_wordcount=2, nmax=1, timeout=10, useAbstract=True):
    """
    Match multiple different keywords from the news with wikipedia articles using advanced methods.

    This matching alogrithm uses keyword co-occurrences which occur together with ``keyword`` in headlines and abstracts for the given dataset of ``articles``.
    Optionally it also searches all subsequences of words which contain the ``keyword``. Then it computes a final query from this information at sends it to the API.

    Notes
    -----
    1.) THIS IS AN OUTDATED VERSION WITH QUADRATIC RUNTIME COMPLEXITY TO RECORD THE DEVELOPMENT PROCESS, USE ``GROUPMATCH`` INSTEAD.
    2.) This implementation is not deterministic, the wikipedia API returns different results within hours.
    3.) If optional parameter ``dates`` gets used, only articles which already existed at ``dates`` will be returned, which increases the runtime 
    in certain circumstances significantly. Make sure to use the parameter ``timeout`` in this case, to limit the runtime for a single query.
    4.) Using ``restore_keyword`` decreases performance significantly, but does not seem to improve the quality noticeably.

    Parameters
    ----------
    keywords : list of str
        List of keywords in ``articles``.
    articles : dict
        Dict of news articles in JSON format.
    restore_keyword : bool
        Specifies whether keyword neighbors should additionally be searched (default is False, see ``restore_keyword`` function).
    dates : list of datetime.date
        Results are limited to articles which already existed at correspnding value of ``dates`` (default is None, see Notes).
    cooc_daterange : int
        Symmetric date range around ``date`` for searching co-occurring keywords (default is None: search in whole article data).
    cooc_wordcount : int
        Specifies how many most co-occurring keywords will be used for searchig related wiki articles (default is 2).
    nmax : int
        Specifies the maximum number of related wikipedia articles which should be returned (default is 1: only return best match).
    timeout : int
        Limits the runtime for this query to ``timeout`` seconds. When exceeding the threshold, intermediate results will be returned (default is 10).
    useAbstract : bool
        Specifies whether the abstract should also be used - only available for NYT (default is True).

    Returns
    -------
    dict
        Dict containing for each keyword the computed advanced query for the API and the corresponding result. 

    """
    matching = {}
    done = set()
    for keyword in keywords:
        skip = False
        for el in done:
            if keyword in el:
                skip = True
        if not skip:
            if cooc_daterange == None:
                date = None
                cooc = mng.get_cooccurrences(keyword, articles, useAbstract=useAbstract)
                if restore_keyword:
                    restored = mng.restore_keyword(keyword, articles)[0][0]
            else:
                date = dates[keywords.index(keyword)]
                start = date - timedelta(days=cooc_daterange)
                end = date + timedelta(days=cooc_daterange)
                cooc = mng.get_cooccurrences(keyword, articles, start=start, end=end, useAbstract=useAbstract)
                if restore_keyword:
                    restored = mng.restore_keyword(keyword, articles, start=start, end=end, useAbstract=useAbstract)[0][0]
            cooc = cooc[:cooc_wordcount]
            if restore_keyword:
                query = set(restored.split())
                for el in cooc:
                    query.add(el[0])
                query = " ".join(query)
            else:
                query = keyword
                for el in cooc:
                    query += " " + el[0]
            done.add(query)
            time.sleep(1)
            matching[keyword] = {
                "query": query, 
                "link": wiki.search_articles(query, nmax=nmax, date=date, timeout=timeout)
            }
    return matching
    

#nyt2019 = mng.load_articles("C:/Users/lukas/Documents/GitHub/wikinews/nyt2019.json")
#print(match("trump", nyt2019))
#print(match("trump", nyt2019, restore_keyword=True))