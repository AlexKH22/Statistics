import numpy as np
import Descriptive_statistics as ds


def b_coef(x, y):
    mu_x = ds.mean(x)
    mu_y = ds.mean(y)
    num = sum((x - mu_x) * (y - mu_y))
    den = sum((x - mu_x)**2)

    return num/den


def a_coef(x, y):
    return ds.mean(y) - ds.mean(x) * b_coef(x, y)


def pearson(x, y):
    mu_x = ds.mean(x)
    mu_y = ds.mean(y)
    num = sum((x - mu_x) * (y - mu_y))
    den = np.sqrt(sum((x - mu_x) ** 2) * sum((y - mu_y) ** 2))

    return num / den


x = np.array([0, 1, 2])
y = np.array([0, 2, 2])

print("b: ", b_coef(x, y))
print("a: ", a_coef(x, y))
print("p: ", pearson(x, y))