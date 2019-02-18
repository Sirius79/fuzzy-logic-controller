
def maximum(**kwargs):
    maxim = 0
    max_key = None
    for key, value in kwargs.items():
         if value > maxim:
             max_key = key
             maxim = value
    return max_key, maxim


def get_area(fuel):
    centre = 0
    area = 0
    if fuel == 0:
        area = 50
        centre = 50
    elif fuel == 1:
        area = 100
        centre = 100
    elif fuel == 2:
        area = 175
        centre = 237.5
    elif fuel == 3:
        area = 150
        centre = 350
    elif fuel == 4:
        area = 575
        centre = 616.66
    return centre, area
