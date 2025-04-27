import datetime
from warpeace_prng import WarAndPeacePseudoRandomNumberGenerator
import math

class Point:
    "A class with a x and y coordinate as a point"
    def __init__(self, x=0, y=0):
        "The constructor that set point's coordinate"
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({}, {})".format(self.x,self.y)

class Ellipse:
    "A class that represent an ellipse"
    def __init__(self, focus1 = Point(0,0), focus2 = Point(0,0), longAxis = 2):
        "The constructor that set two foucs and total length of long Axis(2a). Defaul: a circle at origin and radius = 1"
        self.f1 = focus1
        self.f2 = focus2
        if longAxis <= self.distance(self.f1,self.f2):
            print("Long axis length has to larger than the distance between two focuses. \
            \nPlease create object with long axis longer than {}".format(self.distance(self.f1,self.f2)))
        else: self.lA = longAxis

    def __repr__(self):
        return "Ellipse focuses are: {} and {}. The long Axis length is {}.".format(self.f1,self.f2,self.lA)

    def inEllipse(self, Point):
        'calculate if a point is in the ellipse(include)'
        dist1 = self.distance(self.f1,Point)
        dist2 = self.distance(self.f2,Point)
        return (dist1+dist2) <= self.lA

    def distance(self, Foucs, Point):
        'calculate the distance foucs and point'
        return math.sqrt((Foucs.x-Point.x)**2 +(Foucs.y-Point.y)**2)

    def shortAxis(self):
        'calculate the short axis(b) Notice, its half length of short axis'
        self.sA = round(math.sqrt(((self.lA/2)**2) - (self.distance(self.f1,self.f2)/2)**2) ,2)
        return self.sA

class Area:
    '''A class that could draw an rectangle area.
    Could also draw a bigger rectangle area that could includes two Ellipse'''
    def __init__(self, x1=0, x2=0, y1=0, y2=0):
        "The constructor that set the boundary"
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def __repr__(self):
        return "The boundary of this area is: \nx = {}\nx = {}\ny = {}\ny = {}".format(self.x1,self.x2,self.y1,self.y2)

    def twoEllipse(self,e1=Ellipse(),e2=Ellipse()):
        "find a rectangle are that could inculdes two input ellipses"
        # take all x and y coordinates and put them in two lists
        x = [e1.f1.x,e1.f2.x,e2.f1.x,e2.f2.x]
        y = [e1.f1.y,e1.f2.y,e2.f1.y,e2.f2.y]
        # find the half of longest long axis
        halfLong = max(e1.lA,e2.lA)/2
        # find the safe boundary by use min or max plus or minus halfLong
        self.x1 = min(x)-halfLong
        self.x2 = max(x)+halfLong
        self.y1 = min(y)-halfLong
        self.y2 = max(y)+halfLong
        return self.x1,self.x2,self.y1,self.y2

    def proportion(self):
        'return proportion of this area'
        return abs(self.x2-self.x1)*abs(self.y2-self.y1)


def computeOverlapOfEllipses(e1, e2):
    'enter two ellipses and calculate the overlap proportion'
    # create an area object and find the safe boundary for two ellipses and find the proportion of this area
    area = Area()
    x1,x2,y1,y2 = area.twoEllipse(e1,e2)
    prop = area.proportion()
    # create a random number generator, count for the overlap points
    prng = WarAndPeacePseudoRandomNumberGenerator()
    count = 0
    # set how many times we wish to draw a point
    times = 10000
    for i in range(times):
        point = Point(round((x2-x1)*prng.random() + x1, 2),round((y2-y1)*prng.random() + y1, 2))
        if e1.inEllipse(point) and e2.inEllipse(point):
            count += 1
    # return overlap area
    return round((count / times) * prop, 3)

def main():
    # try a circle radius = 1 and radius = 2
    origin = Point(0,0)
    e1 = Ellipse(origin, origin, 2)
    print(' e1 is a circle centered at origin with radius = 1\n')
    e2 = Ellipse(origin, origin, 4)
    print(' e2 is a circle centered at origin with radius = 2\n')
    overlap = computeOverlapOfEllipses(e1,e2)
    print ("The overlap area is area of smaller circle e1: {}\nCompare to the math area 3.142".format(overlap))

    # try the given example
    p1 = Point(2,3)
    p2 = Point(4,3)
    e3 = Ellipse(p1,p2,4)
    print('\n e3 "{}" is created.'.format(e3))
    e4 = Ellipse(p1,p2,6)
    print('\n e4 "{}" is created.'.format(e4))
    # area of an ellipse = pi × a × b
    a = e3.lA/2
    b = e3.shortAxis()
    mathArea = round(math.pi * a * b, 3)
    # the area is the area of smaller ellipse e 4
    overlap1 = computeOverlapOfEllipses(e3,e4)
    print ("\nThe overlap area is area of smaller ellipse e3: {}\nCompare to the math area {}".format(overlap1,mathArea))

    # try test set from Michael
    # not overlapping
    p3 = Point(4,0)
    p4 = Point(6,0)
    p5 = Point(10,0)
    e5 = Ellipse(origin,p3,6)
    print('\n e5 "{}" is created.'.format(e5))
    e6 = Ellipse(p4,p5,6)
    print('\n e6 "{}" is created.'.format(e6))
    overlap2 = computeOverlapOfEllipses(e5,e6)
    print ("\nThe overlap area is: {}\nCompare to the math area 0".format(overlap2))

    # try test set from Michael
    # overlapping - last example
    p6 = Point(6,6)
    p7 = Point(1,8)
    p8 = Point(7,3)
    p9 = Point(9,4)
    e7 = Ellipse(p6,p7,9)
    print('\n e7 "{}" is created.'.format(e7))
    e8 = Ellipse(p8,p9,9)
    print('\n e8 "{}" is created.'.format(e8))
    overlap3 = computeOverlapOfEllipses(e7,e8)
    print ("\nThe overlap area is: {}\nCompare to Michael's result: 13.64".format(overlap3))

main()
