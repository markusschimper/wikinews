from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import time
import datetime
import requests
import logging
import json

def download_articles(api_key, path_results, start, end):
    """
    Downloads TheGuardian article data.

    Downloads the TheGuardian article data between day ``start`` and day ``end`` and stores it at the given path ``path_results``.

    Notes
    -----
    An ``api_key`` can be requested at https://open-platform.theguardian.com/access/.

    Parameters
    ----------
    api_key : str
        API key for accessing the database of TheGuardian.
    path_results : str
        Path on local machine where article dataset should be stored.
    start : datetime.date
        Only searching articles which have been published on or after this day.
    end : datetime.date
        Only searching articles which have been published on or before this day.

    Returns
    -------
    None

    """
    logging.basicConfig(format='%(asctime)s [%(levelname)s] - %(message)s', datefmt='%d-%m-%y %H:%M:%S', level=logging.DEBUG)
    url = "https://content.guardianapis.com/search?from-date={}&to-date={}&order-by=oldest&page-size=200&api-key={}&page=" # https://open-platform.theguardian.com/documentation/
    # translating properties to nyt format:  key = theguardian format, value = nyt format
    properties = {"webTitle": "headline", "webPublicationDate": "pub_date", "webUrl": "web_url", "type": "document_type", "sectionName": "section_name"}
    data = {}
    cur_date = start
    cur_page = 1
    cnt = 1

    logging.info("Starting..")
    while cur_date != end + relativedelta(days=+1):
        log_starttime = datetime.datetime.now()
        if (cur_date.day == 1 or cur_date == start) and cur_page == 1:
            logging.info("Downloading {}/{} ..".format(cur_date.year, cur_date.month))
        response = requests.get(url.format(cur_date, cur_date, api_key) + str(cur_page))
        logging.debug("REQUEST for cnt {} on {} on page {}".format(str(cnt), str(cur_date), str(cur_page)))
        if response.status_code == 200:
            if str(cur_date.year) not in data:
                data[str(cur_date.year)] = {}
                if cur_date != start:
                    logging.info("Caching results as json..")
                    with open(path_results, "w") as fp:
                        json.dump(data, fp)
            if str(cur_date.month) not in data[str(cur_date.year)]:
                data[str(cur_date.year)][str(cur_date.month)] = {}
                cnt = 1
            for article in response.json()["response"]["results"]:
                data[str(cur_date.year)][str(cur_date.month)][str(cnt)] = {}
                for el in properties:
                    if el in article:
                        data[str(cur_date.year)][str(cur_date.month)][str(cnt)][properties[el]] = article[el]
                    else:
                        data[str(cur_date.year)][str(cur_date.month)][str(cnt)][properties[el]] = ""
                cnt += 1
        else:
            logging.error(response.status_code, response.reason)
        log_endtime = datetime.datetime.now()
        log_runtime = (log_endtime - log_starttime)
        if log_runtime < timedelta(seconds=18): 
            logging.debug("Waiting {} seconds".format(18-log_runtime.seconds)) # https://developer.nytimes.com/faq#a11 ( -> max every 17.28 sec a request = max 5000 req/day !!! )
            time.sleep(18-log_runtime.seconds)
        try:
            if response.json()["response"]["pages"] == response.json()["response"]["currentPage"]:
                cur_date += relativedelta(days=+1)
                cur_page = 1
            else:
                cur_page += 1
        except:
            cur_date += relativedelta(days=+1)
            cur_page = 1

    logging.info("Saving results as json..")
    with open(path_results, "w") as fp:
        json.dump(data, fp)

    logging.info("Done!")


# file: theguardian.json ( 01.01.2001 - 01.10.2020 )
#download_articles("__KEY__", "/home/lmoldon/forschungspraktikum/theguardian.json", date(2001, 1, 1), date(2020, 10, 1))
# file: theguardian_partition.json ( 01.01.2001 - 31.01.2001 )
#download_articles("__KEY__", "/home/lmoldon/forschungspraktikum/theguardian_partition.json", date(2001, 1, 1), date(2001, 1, 31))