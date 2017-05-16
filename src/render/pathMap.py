import random
import math
import pygame

class Line():
    lsize = 0
    line = []
    def append(self, point):
        self.line.append(point)
        self.lsize += 1

class SemiCircle():
    ssize = 0
    circle = []
    def append(self, point):
        self.circle.append(point)
        self.ssize += 1

class Point():
        def __init__(self, startx, starty):
            self.x = startx
            self.y = starty



class Path():
    startangle = []
    angleList = [0,30,45,60,90,120,135,150,180,210,225,240,270,300,315,330,360]
    def findpath(self,mpoint):
        path1 = []
        path2 = []
        path3 = []
        path4 = []
        path5 = []

        self.listPoints1 = [] # a set of points
        listPoints2 = [] # another set of points
        #have same number of list points for paths
        #number of paths is up to you
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
            self.r = 50
            if(len(self.startangle) == 0):
                angle = math.radians(self.angleList[random.randint(0,16)])
                self.startangle.append(angle)   
            else:
                s = self.startangle [-1] + math.pi
                angle = s + math.radians(self.angleList[random.randint(0,7)])

            point1 = Point(int(self.r*math.cos(angle))+i.x, int(self.r*math.sin(angle))+i.y)
            point2 = Point(int(self.r*math.cos(angle+math.pi))+i.x, int(self.r*math.sin(angle+math.pi))+i.y)
            self.listPoints1.append(point1)
            self.listPoints1.append(point2)
        
        
        pathway= []
        pp = self.createPath(mpoint)
        for i in pp:
                if type(i) == type(Line()):
                    pathway.extend(i.line)
                if type(i) == type(SemiCircle()):
                    pathway.extend(i.circle)
        return pathway



    #def __init__(self, mpoint):
        #create paths (use list of points to create a path from the beginning of the array to the end)
        #can make multiple paths
        #init should take musical points, then create list points from that
       
        #they will be whatever radius you set from the point
        #the music point must be between the path point   

    def createLine(self, point1, point2):
        line = Line()
        #creates a line between a set of points
        #basically plot a line between point 1 and 
        #record all the points in that line
        #use a for loop to plot all the points between point1 and point2
        #calculate the equation of a line to do this
        hy = (point2.y-point1.y)
        lx = (point2.x-point1.x)
        if lx is 0:
            m = 0
        else:
            m = hy / lx
        b = point1.y - (m*point1.x)
        # yw - y1 / point2.x - point1.x for m
        # for loop
        if ( point1.x > point2.x ):
            for i in range(point2.x, point1.x):
                y = (m*i) + b
                newPoint = Point( int(i), int(y) )
                line.append(newPoint)
        else:
            for i in range(point1.x,point2.x):
                y = (m*i) + b
                newPoint = Point( int(i), int(y) )
                line.append(newPoint)

        newLine = line
        line = None
        return newLine
        # line.append
        # boom

    def distance(self, point1, point2):
        return math.sqrt((point1.x-point2.x)**2+(point1.y-point2.y)**2)

    def between(self, mpoint, point1, point2):
        btw = False
        daCount = 0
        for count, p in enumerate(mpoint):
            dis = self.distance(point1, p) + self.distance(p, point2) == self.distance(point1, point2)
            if (dis is True):
                btw = True
                daCount = count
        return (btw, mpoint[daCount])

    def circlecontact(self,mpoint,point1,point2):
        pygame.init()
        for count,m in enumerate(mpoint):                  
        # Centre of circle
            Q = pygame.math.Vector2(m.x, m.y) 
            r = 50               
        # Radius of circle
            P1 = pygame.math.Vector2(point1.x,point1.y)      
        # Start of line segment
            V = pygame.math.Vector2(point2.x,point2.y)-P1
        # Vector along line segment
            a = V.dot(V)
            b = 2 * V.dot(P1 - Q)
            c = P1.dot(P1) + Q.dot(Q) - 2 * P1.dot(Q) - r**2
            disc = b**2 - 4 * a * c
            if disc < 0:
                return (False, Point(0,0))
            sqrt_disc = math.sqrt(disc)
            t1 = (-b + sqrt_disc) / (2 * a)
            t2 = (-b - sqrt_disc) / (2 * a)
            if not (0 <= t1 <= 1 or 0 <= t2 <= 1):
                return (False,Point(0,0))
            t = max(0, min(1, - b / (2 * a)))
            intersect = P1 + t*V - Q == r
            return (intersect, mpoint[count])

    def createHalfCircle(self, m, point1, point2):
        #creates a half circle with angle and radius
        #x = rcos(angle)
        #y = rsin(angle)
        #radius = distance from point 1 to point 2 / 2
        r = self.r #.distance(point1, point2)/2
        #start angle = sin^-1 ( point1.y / r )
        #end angle = sin^-1 ( point2.y / r )
        #if (point1.y > m.y):
        start = math.acos((m.x-point1.x) / self.r)
        end = start + math.pi
        #else:
            #start = math.acos((m.x-point2.x) / self.r)
            #end = start + math.pi
        #then cycle through angle degrees until you have the points of the circle
        circle = SemiCircle()
        #calculate mpoint
        #mh = point1.x - self.r*math.cos(start)
        #mk = point1.y - self.r*math.sin(start)
        mh = m.x
        mk = m.y

        nstart = math.floor(math.degrees(start))
        nend = math.floor(math.degrees(end))
        for i in range(nstart, nend):
            point = Point(int(r*math.cos(math.radians(i)))+mh, int(r*math.sin(math.radians(i)))+mk)
            circle.append(point)
        newCircle = circle
        circle = None
        return newCircle

    def createPath(self, mpoint):
        path1 = []
        #uses listpoints to create a path
        for count,i in enumerate(self.listPoints1):
            halfcreate=False
            if count+1 != len(self.listPoints1):
                isBetween, m = self.between(mpoint,i,self.listPoints1[count+1])
                #isBetween, m = self.circlecontact(mpoint,i,self.listPoints1[count+1])
                if isBetween:
                    path1.append(self.createHalfCircle(m, i, self.listPoints1[count+1]))
                    halfcreate=True
                else:
                    path1.append(self.createLine(i,self.listPoints1[count+1]))
            else:
                isBetween, m = self.between(mpoint,i,self.listPoints1[0])
                #isBetween, m = self.circlecontact(mpoint,i,self.listPoints1[0])
                if isBetween:
                    path1.append(self.createHalfCircle(m, i, self.listPoints1[0]))
                    halfcreate=True
                else:
                    path1.append(self.createLine(i,self.listPoints1[0]))   
        return path1                           
        #stores in path
        #half cirlces are made when a music point is between two line points

        #access internal listpoint
        #for loop through
        #if there is a music point between two list points
        #create halfcirlce
        #otherwise, create line
   
            