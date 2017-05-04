import pygame.random

class Path():
    path1 = []
    path2 = []
    path3 = []
    path4 = []
    path5 = []

    listPoints1 = ['''define a set of points here'''] # a set of points
    listPoints2 = [] # another set of points
    #have same number of list points for paths
    #number of paths is up to you
    
    class Point():
        def __init__(self, startx, starty):
            self.x = startx
            self.y = starty

    def __init__(self, mpoint):
        #create paths (use list of points to create a path from the beginning of the array to the end)
        #can make multiple paths
        #init should take musical points, then create list points from that
        r = 20
        #they will be whatever radius you set from the point
        #the music point must be between the path point

        #loop through music points
        #take one music point
        #create two points
        #random angle, create point 1
        #angle + 180, create p2
        #cos and sin of an angle
        #static radius value
        #angles must be parallel
        #can draw line through all three points
        #if random angle used, add 180 for other angle
        #append p1 and p2 
        for i in mpoint:
            angle = random.randint(0,360) #2*pi*random
            point1 = Point(rcos(angle), rsin(angle))
            point2 = Point(rcos(angle), rsin(angle+180))
            listpoint1.append (point1)
            listpoint1.apeend (point2)
        
        self.createPath(mpoint)
        

    class Line():
        size = 0
        line = []
        def append(point):
            line.append(point)
            size += 1

    class SemiCircle():
        size = 0
        circle = []
        def append(point):
            circle.append(point)
            size += 1

    def createLine(point1, point2):
        line = Line()
        #creates a line between a set of points
        #basically plot a line between point 1 and 
        #record all the points in that line
        #use a for loop to plot all the points between point1 and point2
        #calculate the equation of a line to do this
        m = point2.y-point1.y/point1.x-point2.x
        b = point1.y - m*point1.x
        # yw - y1 / point2.x - point1.x for m
        # for loop
        for i in range(point1.x,point2.x):
            y = (point1.x+1) * m + b
            line.append(Point(point1.x+1,y))
        return line
        # line.append
        # boom

    def distance(point1, point2):
            return sqrt((points1.x-points2.x)*2+(points1.y-points2.y))

    def between (mpoint,point1,point2):
        return distance(point1,mpoint) + distance(mpoint,point2) == distance(point1,point2)

    def createHalfCircle(point1, point2):
        #creates a half circle with angle and radius
        #x = rcos(angle)
        #y = rsin(angle)
        #radius = distance from point 1 to point 2 / 2
        r = distance()/2  
        #start angle = sin^-1 ( point1.y / r )
        start = sin^-1 (point1.y / r)
        #end angle = sin^-1 ( point2.y / r )
        end = sin^-1 (point2.y / r)
        #then cycle through angle degrees until you have the points of the circle
        circle = SemiCircle()
        for i in range(start,end):
            point = Point(rcos(i),rsin(i))
            circle.append(point)
        return circle

    def createPath(mpoint):
        #uses listpoints to create a path
         for count,i in enumerate(listPoints1):
             halfcreate=False
             for m in mpoint:
                 if count != listPoints1.size:
                    if (between(m,i,i+1)):
                     path1.append(createHalfCircle(i,i+1))
                     halfcreate=True
                 else:
                    if (between(m,i,listPoints1[0])):
                     path1.append(createHalfCircle(i,listPoints1[0]))
                     halfcreate=True
             if count != listPoints1.size:
                if halfcreate == False:
                   path1.append(createLine(i,i+1))
             else:
                if halfcreate == False:
                   path1.append(createLine(i,listPoints1[0]))                              
        #stores in path
        #half cirlces are made when a music point is between two line points

        #access internal listpoint
        #for loop through
        #if there is a music point between two list points
        #create halfcirlce
        #otherwise, create line
   
            