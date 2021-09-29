from datetime import date, timedelta
import time
import datetime
import requests

def get_counts(title, start, end, email, language_edition="en"):
    """
    Get the daily pageviews of an wikipedia article (uses wikipedia API).

    Returns the daily pageviews of the wikipedia article ``title`` between day ``start`` and day ``end`` in the language ``language_edition``.

    Notes
    -----
    1.) Do not make more than one api function call per second due to given request limits by wikipedia. 
    2.) If the function returns an empty list (but the article exists online), then most likely the article was created after day ``end```.  
    3.) We only consider English wikipedia articles in our analysis.

    Parameters
    ----------
    title : str
        Title of the wikipedia article (https://en.wikipedia.org/wiki/``title``).
    start : datetime.date
        First day of pageview statistic.
    end : datetime.date
        Last day of pageview statistic.
    email : str
        Your personal or institutional e-mail address for the request header (providing the possibility to be contacted by Wikipedia)
    language_edition : str
        Selector for the language edition of wikipedia (default is ``en`` for English, see Notes).

    Returns
    -------
    list of datetime.date
        list of daily timestamps.
    list of int
        list of pageview counts for that day (same position as in first list).

    """
    time.sleep(1)
    timestamp_list = []
    viewcount_list = []
    url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/{}.wikipedia/all-access/all-agents/{}/daily/{}/{}" # https://www.mediawiki.org/wiki/API:Etiquette
    header = {
    'User-Agent': 'WikipediaNews 1.0',
    'From': email 
    }
    url_start = str(start).replace("-","")
    url_end = str(end).replace("-","")
    response = requests.get(url.format(language_edition, title, url_start, url_end), headers=header)
    if response.status_code == 200:
        try:
            for item in response.json()["items"]:
                timestamp_str = item["timestamp"]
                datetime = date(int(timestamp_str[:4]), int(timestamp_str[4:6]), int(timestamp_str[6:8]))
                timestamp_list.append(datetime)
                viewcount_list.append(item["views"])
        except KeyError:
            return [], []
    else:
        #print(response.status_code, response.reason)
        return None
    return timestamp_list, viewcount_list

def search_articles(keywords, email, nmax=10, date=None, timeout=10):
    """
    Get ranked search results of wikipedia articles for given keywords belonging to the same topic (uses wikipedia API).

    Returns a ranked dict with ``nmax`` entries of wikipedia articles as search result for the query ``keywords``. If multiple keywords are
    used, then all ``keywords`` should belong to the same topic.

    Notes
    -----
    1.) Do not make more than one api function call per second due to given request limits by wikipedia. 
    2.) This implementation is not deterministic, the API returns different results within hours.
    3.) If optional parameter ``date`` gets used, only articles which already existed at ``date`` will be returned, which increases the runtime 
    in certain circumstances significantly. Make sure to use the parameter ``timeout`` in this case, to limit the runtime for a single query.

    Parameters
    ----------
    keywords : str or list of str
        Keyword(s) for the query (argument for the search).
    email : str
        Your personal or institutional e-mail address for the request header (providing the possibility to be contacted by Wikipedia)
    nmax : int
        Maximum number of wikipedia articles which should be returned (can be less depending on number of found results).
    date : datetime.date
        Results are limited to articles which already existed at ``date`` (default is None, see Notes).
    timeout : int
        Limits the runtime for this query to ``timeout`` seconds. When exceeding the threshold, intermediate results will be returned.
    
    Returns
    -------
    dict
        Results of the API search (key represents ranking: starting at 1 for best match, up to ``nmax``)

    """
    start = datetime.datetime.now()
    url = "https://en.wikipedia.org/w/api.php"
    if type(keywords) == list:
        keywords = " ".join(keywords)
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": keywords
    }
    header = {
    'User-Agent': 'WikipediaNews 1.0',
    'From': email 
    }
    response = requests.get(url=url, params=params, headers=header)
    if response.status_code == 200:
        ranking = {}
        i = 1
        try:
            for item in response.json()["query"]["search"]:
                now = datetime.datetime.now()
                if start +  timedelta(seconds=timeout) < now:
                    break
                elif "disambiguation" not in item["title"] and i <= nmax:
                    if date == None:
                        ranking[i] = item["title"].replace(" ", "_")
                        i += 1
                    else:
                        time.sleep(1)
                        if get_creationdate(item["title"]) <= date:
                            ranking[i] = item["title"].replace(" ", "_")
                            i += 1
        except KeyError:
            return {}
    else:
        print(response.status_code, response.reason)
        return {}
    return ranking

def get_creationdate(title, email):
    """
    Get the date of creation of a given wikipedia article.

    Notes
    -----
    Do not make more than one api function call per second due to given request limits by wikipedia.
    
    Parameters
    ----------
    title : str
        Title of the wikipedia article (https://en.wikipedia.org/wiki/``title``).
    email : str
        Your personal or institutional e-mail address for the request header (providing the possibility to be contacted by Wikipedia)
    
    Returns
    -------
    datetime.date
        creation date of the article.
        
    """
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "prop": "revisions",
        "titles": title,
        "rvdir": "newer",
        "rvlimit": 1,
        "rvprop": "timestamp|user",
        "rvslots": "main",
        "formatversion": "2",
        "format": "json"
    }
    header = {
    'User-Agent': 'WikipediaNews 1.0',
    'From': email 
    }
    response = requests.get(url=url, params=params, headers=header)
    if response.status_code == 200:
        i = 1
        try:
            timestamp = response.json()["query"]["pages"][0]["revisions"][0]["timestamp"]
            return datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ").date()
        except KeyError:
            return None
    else:
        print(response.status_code, response.reason)
        return None


print(search_articles("9/11"))
#print(search_articles(["9/11", "attacks", "New", "York"], email))
#print(get_creationdate("September_11_attacks"), email)
#print(get_creationdate("Aftermath_of_the_September_11_attacks"), email)
#print(search_articles(["9/11", "attacks", "New", "York"], email, date=date(2001,11,22))) # e.g. on 2001-11-22 9/11 was mentioned in the news, not all related articles created yet