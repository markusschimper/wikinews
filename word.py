import timeseries

class Word:
    '''
    Class to add additional information to a keyword like timeseries of the news and Wikipedia, co-occurrences and the matched Wikipedia site.

    '''
    def __init__(self,keyword,ts_wiki=None,ts_articles=None,coocKeywords=[],wikipediaSite=""):
        self.keyword = keyword
        self.ts_wiki = ts_wiki
        self.ts_articles = ts_articles
        self.coocKeywords = coocKeywords
        self.wikipediaSite = wikipediaSite