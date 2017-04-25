import random

radius = 200
rangeX = (0, 500)
rangeY = (0, 500)
qty = 1  # quantity of points

#create a set of all points within 200 of the origin

class Point():
    def __init__(self, startx, starty):
        self.x = startx
        self.y = starty

def create():
    deltas = set()
    for x in range(-radius, radius+1):
        for y in range(-radius, radius+1):
            if x*x + y*y <= radius*radius:
                deltas.add((x,y))

    randPoints = []
    excluded = set()
    i = 0
    while i<qty:
        x = random.randrange(*rangeX)
        y = random.randrange(*rangeY)
        if (x,y) in excluded: 
            continue
        randPoints.append(Point(x,y))
        i += 1
        excluded.update((x+dx, y+dy) for (dx,dy) in deltas)

    points = []
    for d in range(5):
        points.append( Point(random.randint(-1,100), random.randint(-1,100)) )

    return points