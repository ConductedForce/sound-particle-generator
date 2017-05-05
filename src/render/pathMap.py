import random
import math

class Point():
        def __init__(self, startx, starty):
            self.x = startx
            self.y = starty

class Path():
    path1 = []
    path2 = []
    path3 = []
    path4 = []
    path5 = []

    listPoints1 = [] # a set of points
    listPoints2 = [] # another set of points
    #have same number of list points for paths
    #number of paths is up to you
    
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
            point1 = Point(int(r*math.cos(angle)), int(r*math.sin(angle)))
            point2 = Point(int(r*math.cos(angle)), int(r*math.sin(angle+180)))
            self.listPoints1.append(point1)
            self.listPoints1.append(point2)
        
        self.createPath(mpoint)
        

    class Line():
        size = 0
        line = []
        def append(self, Point):
            self.line.append(Point)
            self.size += 1

    class SemiCircle():
        size = 0
        circle = []
        def append(self, point):
            self.circle.append(point)
            self.size += 1

    def createLine(self, point1, point2):
        line = self.Line()
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
            newPoint = Point( int(point1.x+1), int(y) )
            line.append(newPoint)
        return line
        # line.append
        # boom

    def distance(self, point1, point2):
            return math.sqrt((point1.x-point2.x)*2+(point1.y-point2.y))

    def between(self, mpoint,point1,point2):
        return self.distance(point1,mpoint) + self.distance(mpoint,point2) == self.distance(point1,point2)

    def createHalfCircle(self, point1, point2):
        #creates a half circle with angle and radius
        #x = rcos(angle)
        #y = rsin(angle)
        #radius = distance from point 1 to point 2 / 2
        r = self.distance()/2  
        #start angle = sin^-1 ( point1.y / r )
        start = math.sin^-1 (point1.y / r)
        #end angle = sin^-1 ( point2.y / r )
        end = math.sin^-1 (point2.y / r)
        #then cycle through angle degrees until you have the points of the circle
        circle = self.SemiCircle()
        for i in range(start,end):
            point = Point(int(r*math.cos(i)), int(r*math.sin(i)))
            circle.append(point)
        return circle

    def createPath(self, mpoint):
        #uses listpoints to create a path
         for count,i in enumerate(self.listPoints1):
             halfcreate=False
             for m in mpoint:
                 if count+1 != len(self.listPoints1):
                    if self.between(m,i,self.listPoints1[count+1]):
                     path1.append(self.createHalfCircle(i,self.listPoints1[count+1]))
                     halfcreate=True
                 else:
                    if self.between(m,i,self.listPoints1[0]):
                     self.path1.append(self.createHalfCircle(i,self.listPoints1[0]))
                     halfcreate=True
             if count+1 != len(self.listPoints1):
                if halfcreate == False:
                   self.path1.append(self.createLine(i,self.listPoints1[count+1]))
             else:
                if halfcreate == False:
                   self.path1.append(self.createLine(i,self.listPoints1[0]))                              
        #stores in path
        #half cirlces are made when a music point is between two line points

        #access internal listpoint
        #for loop through
        #if there is a music point between two list points
        #create halfcirlce
        #otherwise, create line
   
            