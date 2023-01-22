import numpy as np
from scipy.special import comb 
class Bez():
    def __init__(self):
        self.r = lambda i, n, t: comb(n, i) * ( t**(n-i) ) * (1 - t)**i
        self.points = []
        self.box = []
        self.box2 = []

    def _curve(self, points, am_c):
        nPoints = len(points)
        xPoints = np.array([p[0] for p in points])
        yPoints = np.array([p[1] for p in points])
        t = np.linspace(0.0, 1.0, am_c)
        polynomial_array = np.array([self.r(i, nPoints-1, t) for i in range(0, nPoints)])
        xvals = np.dot(xPoints, polynomial_array)
        yvals = np.dot(yPoints, polynomial_array)
        return xvals, yvals

    def _create(self, points, am_c):
        x,y = self._curve(points, am_c)
        for i in range(len(x)):
            x_p, y_p = x[i], y[i]
            self.points.append([x_p-5,y_p-5])

        return self.points

    def _box(self, points:list=[], thickness:int=10):
        self.p = points
        #[[0,0],[40,40]]

        for x in range(abs(self.p[0][0]-self.p[1][0])):
            for y in range(abs(self.p[0][1]-self.p[1][1])):
                self.box.append([x+1,y+1])
                self.box2.append([x+1,y+1])

        for point in points:
            for coord in point:
                points[points.index(point)][point.index(coord)] += 5

        for x in range(abs(self.p[0][0]-self.p[1][0])):
            for y in range(abs(self.p[0][1]-self.p[1][1])):
                if [x-thickness,y-thickness] in self.box:
                    self.box.remove([x-thickness,y-thickness])
                if [x+thickness,y+thickness] in self.box2:
                    self.box2.remove([x+thickness,y+thickness])
        for x in self.box2:
            self.box.append(x)
        r = []
        for x in self.box:
            if x not in r:
                r.append(x)
        return r