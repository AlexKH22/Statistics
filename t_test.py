import numpy as np


def t(sample1, sample2):
    numerator = np.mean(sample1) - np.mean(sample2)
    denominator = np.sqrt(np.var(sample1)/len(sample1) - np.var(sample2)/len(sample2))

    return numerator/denominator


def nu(sample1, sample2):
    numerator = (np.var(sample1) / len(sample1) - np.var(sample2) / len(sample2))**2
    denominator = np.var(sample1)**2 / (len(sample1)**2 * (len(sample1) - 1)) + np.var(sample2)**2 / (len(sample2)**2 * (len(sample2) - 1))

    return numerator / denominator


# sample1 =