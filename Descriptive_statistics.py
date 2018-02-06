from math import sqrt

import time

sample = [0, 1]


def mean(data):
    return sum(data)/len(data)


def newmean(mu, count, new):
    numerator = count * mu + sum(new)
    denominator = count + len(new)

    return numerator/denominator


def mode(data):
    m = max([data.count(a) for a in data])
    return [x for x in data if data.count(x) == m][0] if m > 1 else None


def median(data):
    sorted_list = sorted(data)
    length = len(sorted_list)
    center = length // 2

    if length == 1:
        return sorted_list[0]

    elif length % 2 == 0:
        return sum(sorted_list[center - 1: center + 1]) / 2.0

    else:
        return sorted_list[center]


def variance(data):
    mu = mean(data)
    return mean([(x - mu)**2 for x in data])


def stddev(data):
    return sqrt(variance(data))


def maxlikelihood(dist, data):
    prob = 1
    for item in data:
        prob *= dist[item]

    return prob


def confidence_interval(data, t=1.96):
    ci = t * sqrt(variance(data)/len(data))
    print("The average value is {} +/- {}".format(mean(data), ci))
    print("Interval: {} - {}".format(mean(data)-ci, mean(data)+ci))

    return ci


def confidence_interval_for_prob(data, index):
    prob = data[index]/sum(data)
    ci = 1.96 * sqrt((prob * (1 - prob)) / sum(data))
    print("The value is {}% +/- {}%".format(prob * 100, ci * 100))

    return ci


def hypothesistest(data, h):
    mu = mean(data)
    ci = confidence_interval(data)

    return abs(h - mu) <= ci


# print(variance(sample))
#
# print(newmean(10, 5, [4]))
#
#
# dist = {'A': 0.2, 'B': 0.2, 'C': 0.2, 'D': 0.2, 'E': 0.2}
# sample = 'ABCEDDECAB'
#
# print(maxlikelihood(dist, sample))
#
# dist = {'Z':0.6,'X':0.333,'Y':0.067}
# sample = 'ZXYYZXYXYZY'
#
# print(maxlikelihood(dist, sample))
#
# confidence_interval(400*[0] + 600*[1])
#
# data = 4*[21] + 6*[24] + 7*[26] + 11*[29] + 2*[40]
#
# print(mean(data))
# print(variance(data))
# confidence_interval(data)

# data = [i for i in range(199, 205)]
# h = 201
#
# print(hypothesistest(data, h))

# data = [55, 45]
# print(confidence_interval_for_prob(data, 0))

# confidence_interval(4950*[1] + 5050*[0])

# data = [0.79, 0.7, 0.73, 0.66, 0.65, 0.7, 0.74, 0.81, 0.71, 0.7]
# confidence_interval(data, t=2.262)