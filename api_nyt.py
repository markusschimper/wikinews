from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import time
import datetime
import requests
import logging
import json

def download_articles(api_key, path_results, start, end):
    """
    Downloads NYT article data.

    Downloads the NYT article data between day ``start`` and day ``end`` and stores it at the given path ``path_results``.

    Notes
    -----
    An ``api_key`` can be requested at https://developer.nytimes.com/get-started.

    Parameters
    ----------
    api_key : str
        API key for accessing the database of NYT.
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
    logging.basicConfig(format='%(asctime)s [%(levelname)s] - %(message)s', datefmt='%d-%m-%y %H:%M:%S', level=logging.INFO)
    url = "https://api.nytimes.com/svc/archive/v1/{}/{}.json?api-key={}" # see https://developer.nytimes.com/docs/archive-product/1/overview
    properties = ["headline", "pub_date", "web_url", "abstract", "lead_paragraph", "keywords", "document_type", "type_of_material", "word_count", "section_name"]
    data = {}
    cur_date = start

    logging.info("Starting..")
    while cur_date != end + relativedelta(months=+1):
        log_starttime = datetime.datetime.now()
        logging.info("Downloading {}/{} ..".format(cur_date.year, cur_date.month))
        response = requests.get(url.format(cur_date.year, cur_date.month, api_key))
        if response.status_code == 200:
            if str(cur_date.year) not in data:
                data[str(cur_date.year)] = {}
            data[str(cur_date.year)][str(cur_date.month)] = {}
            cnt = 1
            for article in response.json()["response"]["docs"]:
                data[str(cur_date.year)][str(cur_date.month)][str(cnt)] = {}
                for el in properties:
                    if el in article:
                        if el == "headline":
                            data[str(cur_date.year)][str(cur_date.month)][str(cnt)]["headline"] = article["headline"]["main"]
                        else:
                            data[str(cur_date.year)][str(cur_date.month)][str(cnt)][el] = article[el]
                    else:
                        data[str(cur_date.year)][str(cur_date.month)][str(cnt)][el] = ""
                cnt += 1
        else:
            logging.error(response.status_code, response.reason)
        log_endtime = datetime.datetime.now()
        log_runtime = (log_endtime - log_starttime)
        if log_runtime < timedelta(seconds=6): 
            logging.debug("Waiting {} seconds".format(6-log_runtime.seconds)) # https://developer.nytimes.com/faq#a11 ( -> max 10 req/min AND 4000 req/day !!! )
            time.sleep(6-log_runtime.seconds)
        cur_date += relativedelta(months=+1)

    logging.info("Saving results as json..")
    with open(path_results, "w") as fp:
        json.dump(data, fp)

    logging.info("Done!")


# file: nyt.json ( 01.01.2001 - 01.10.2020 )
#download_articles("__KEY__", "/home/lmoldon/forschungspraktikum/nyt.json", date(2001, 1, 1), date(2020, 10, 1))
# file: nyt_partition.json ( 01.01.2001 - 31.01.2001 ) (start = end (!) due to monthly scraping/download)
#download_articles("__KEY__", "/home/lmoldon/forschungspraktikum/nyt_partition.json", date(2001, 1, 1), date(2001, 1, 1))