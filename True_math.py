from math import inf

def divide(a,b):
    if b == 0:
        return inf
    else:
        return round(a/b, 2)