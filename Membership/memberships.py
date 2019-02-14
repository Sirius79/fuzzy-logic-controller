import math


def trapezoid(x, a, b, c, d):
    numlist = []
    if a != b:
        numlist.append(float(x - a) / (b - a))
    if c != d:
        numlist.append(float(d - x) / (d - c))
    numlist.append(1.0)
    return round(max(min(numlist), 0.0), 3)


def gaussian(x, c, sig):
    return math.exp((-1 / 2) * ((x - c) / sig) * ((x - c) / sig))


def sigmoid(x, a, c):
    return 1 / (1 + math.exp(-a * (x - c)))


def bell(x, a, b, c):
    return 1 / (1 + math.pow(abs((x - c) / a), 2 * b))
