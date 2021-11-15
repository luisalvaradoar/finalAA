class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def Qadrentro(polygon, point):
    A = []
    B = []
    C = []  
    for i in range(len(polygon)):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % len(polygon)]

        a = -(p2.y - p1.y)
        b = p2.x - p1.x
        c = -(a * p1.x + b * p1.y)

        A.append(a)
        B.append(b)
        C.append(c)

    D = []
    for i in range(len(A)):
        d = A[i] * point.x + B[i] * point.y + C[i]
        D.append(d)

    t1 = all(d >= 0 for d in D)
    t2 = all(d <= 0 for d in D)
    return t1 or t2

if __name__ == '__main__':
    N = 3
    pol_ver_x = (0,1,2)
    pol_ver_y = (0,2,0)
    polygon = []
    for i in range(N):
        polygon.append(Point(pol_ver_x[i], pol_ver_y[i]))
    point_x = 1
    point_y = 1
    print(Qadrentro(polygon, Point(point_x, point_y))) # returns True
