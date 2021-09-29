import matplotlib.pyplot as plt
import api_wikipedia as wiki
from datetime import date
import matplotlib.backends.backend_pdf
import matplotlib.pylab as pl
import matplotlib.gridspec as gridspec
import statistics

def plot_wikipedia(title, start, end, language_edition="en"):
    """
    Plot daily wikipedia pageview counts for a given article.

    Plots the daily wikipedia pageview counts between days ``start`` and ``end`` for an article with given ``title``.

    Notes
    -----
    We only consider English wikipedia articles in our analysis.

    Parameters
    ----------
    title : str
        Title of the wikipedia article (https://en.wikipedia.org/wiki/``title``).
    start : datetime.date
        First day of plot.
    end : datetime.date
        Last day of plot.
    language_edition : str
        Selector for the language edition of wikipedia (default is ``en`` for English, see Notes).
    
    Returns
    -------
    None

    """
    x, y = wiki.get_counts(title,start,end, language_edition=language_edition)
    if x != [] and y != []:
        plt.figure(figsize=(10,10))
        plt.plot(x,y)
        plt.title("{} ({})".format(title, language_edition))
        plt.show()

def plot_dataset(word,dataset,timepoints):
    """
    Plot any data with finite amount of datapoints.

    Parameters
    ----------
    word : str
        Title of the plot (e.g. keyword).
    dataset: list of int
        Values for the plot (y axis).
    timepoints: list of Timepoint
        Timepoints for the plot (x axis).
    
    Returns
    -------
    None

    """
    if timepoints != [] and dataset != []:
        plt.figure(figsize=(10,10))
        plt.plot(timepoints,dataset)
        plt.title(word)
        plt.show()

def createPDFwithBothPlots(word):
    """
    Creates a png file with articles and wikipedia plot and their correlation. Output will be saved in correlation subfolder

    Parameters
    ----------
    word : word object
    
    Returns
    -------
    None

    """
    fig = plt.figure(figsize=(5,5))
    
    axis1 = fig.add_subplot(211)
    plt.xticks(rotation=30)
    plt.plot(word.ts_articles.getDates(),word.ts_articles.getCounts())
    plt.title(word.keyword)
    
    fig.subplots_adjust(hspace=0.65, wspace=0.4)

    axis2 = fig.add_subplot(212)
    plt.xticks(rotation=30)
    x, y = wiki.get_counts(word.wikipediaSite,word.ts_articles.getDates()[0],word.ts_articles.getDates()[-1], language_edition="en")
    if x != [] and y != []:
        plt.plot(x,y)
        plt.title(format(word.wikipediaSite))
        axis2.set_xlabel("Correlation: " + str(statistics.getCorrelation(word.ts_articles.getCounts(),word.ts_wiki.getCounts())),labelpad=20)
        #plt.show()
    

    plt.tight_layout(pad=10, w_pad=10, h_pad=10)
    plt.gcf().subplots_adjust(bottom=0.22)
    fig.savefig('./correlation_shuffled/' + word.keyword + '.png')
    

    
# seasonality pattern
# plot_wikipedia("Santa_Claus", date(2015,7,1), date(2018,12,31))

# random pattern
# plot_wikipedia("Berlin", date(2015,7,1), date(2018,12,31))

# repetitive (but not seasonal) pattern
# plot_wikipedia("UEFA_European_Championship", date(2015,7,1), date(2018,12,31))

# Influence of trigger events / historical incidents
# plot_wikipedia("Coronavirus", date(2015,7,1), date(2020,10,20))

# Influence of complex / not trivial connections
# -> "Stellar corona" is an aura of plasma that surrounds the sun (but has nothing to do with the coronavirus besides naming)
# plot_wikipedia("Stellar_corona", date(2015,7,1), date(2020,10,20))