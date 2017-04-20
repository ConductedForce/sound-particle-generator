import random

radius = 200
rangeX = (0, 2500)
rangeY = (0, 2500)
qty = 100  # quantity of points

#create a set of all points within 200 of the origin

class Particle():
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
        randPoints.append(Particle(x,y))
        i += 1
        excluded.update((x+dx, y+dy) for (dx,dy) in deltas)
    return randPoints