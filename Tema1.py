from math import sqrt

def d(x, y):
    return sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

def distancia_Hausdorff(X, Y):
    return max(max(min(d(x, y) for y in Y) for x in X), max(min(d(x, y) for x in X) for y in Y))