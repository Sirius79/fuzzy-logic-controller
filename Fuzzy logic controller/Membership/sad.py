from . import memberships as m


def speed(x):
    out = list()
    out.append(m.trapezoid(x, 0, 0, 20, 30))
    out.append(m.trapezoid(x, 20, 30, 40, 45))
    out.append(m.trapezoid(x, 40, 45, 60, 80))
    out.append(m.trapezoid(x, 60, 80, 90, 100))
    out.append(m.trapezoid(x, 90, 100, 150, 150))
    return out


def acceleration(x):
    out = list()
    out.append(m.trapezoid(x, -80, -80, -10, 0))
    out.append(m.trapezoid(x, -10, 0, 0, 10))
    out.append(m.trapezoid(x, 0, 10, 80, 80))
    return out


def distance(x):
    out = list()
    out.append(m.trapezoid(x, 0, 0, 0, 5))
    out.append(m.trapezoid(x, 0, 5, 15, 20))
    out.append(m.trapezoid(x, 15, 20, 28, 35))
    out.append(m.trapezoid(x, 28, 35, 50, 50))
    return out


def fuel(rule, x):
    out = 0
    if rule == 0:
        out = m.trapezoid(x, 0, 0, 0, 100)
    elif rule == 1:
        out = m.trapezoid(x, 0, 100, 100, 200)
    elif rule == 2:
        out = m.trapezoid(x, 100, 200, 300, 350)
    elif rule == 3:
        out = m.trapezoid(x, 200, 350, 350, 500)
    elif rule == 4:
        out = m.trapezoid(x, 350, 500, 1000, 1000)
    return out

