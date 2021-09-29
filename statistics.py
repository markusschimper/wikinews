import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def getVariance(dataset):
    """
    Computes the variance (see ``numpy.var``).

    """
    return np.var(dataset)

def findOutliers(dataset):
    """
    Returns all outliers in a given dataset, which are not within a symmetric range of 3 * standard deviation around the mean value.

    """
    mean = np.mean(dataset)
    std = np.std(dataset)
    out = std*3
    lowerLimit = mean-out
    upperLimit = mean+out
    
    outliers=[]
    for datapoint in dataset:
        if datapoint > upperLimit or datapoint < lowerLimit:
            outliers.append(datapoint)
    return outliers

def getCorrelation(x,y):
    """
    Computes the pearson correlation coefficient (see ``scipy.stats.pearsonr``).

    """
    return stats.pearsonr(x,y)

def mean_confidence_interval(data, confidence=0.95):
    """
    Computes the mean and the confidence interval (see ``scipy.stats.t``).

    """
    # Modified version of https://stackoverflow.com/questions/15033511/compute-a-confidence-interval-from-sample-data
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), stats.sem(a)
    h = se * stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h