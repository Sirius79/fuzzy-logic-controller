from memberships import *

def speed(x):
    out = []
    out.append(trapezoid(x, 0, 0, 20, 30))
    out.append(trapezoid(x, 20, 30, 40, 45))
    out.append(trapezoid(x, 40, 45, 60, 80))
    out.append(trapezoid(x, 60, 80, 90, 100))
    out.append(trapezoid(x, 90, 100, 150, 150))
    return out


def acceleration(x):
    out = []
    out.append(trapezoid(x, -80, -80, -10, 0))
    out.append(trapezoid(x, -10, 0, 0, 10))
    out.append(trapezoid(x, 0, 10, 80, 80))
    return out


def distance(x):
    out = []
    out.append(trapezoid(x, 0, 0, 0, 5))
    out.append(trapezoid(x, 0, 5, 15, 20))
    out.append(trapezoid(x, 15, 20, 28, 35))
    out.append(trapezoid(x, 28, 35, 50, 50))
    return out

