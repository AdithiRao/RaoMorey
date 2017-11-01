class Point:
    def __init__(self,xpos,ypos):
        self.x=xpos
        self.y=ypos
        self.location=(xpos,ypos)
    def dot(self,other):
        return self.x*other.x+self.y*other.y

class Segment:
    def __init__(self,Point1,Point2):
        self.init=Point1
        self.fin=Point2
    def length(self):
        return distance(self.init,self.fin)

def distance(point1,point2):
    return ((point1.x-point2.x)**2+(point1.y-point2.y)**2)**0.5

def intersect(line1,line2):
    x1=line1.init.x
    x2=line1.fin.x
    x3=line2.init.x
    x4=line2.fin.x

    y1=line1.init.y
    y2=line1.fin.y
    y3=line2.init.y
    y4=line2.fin.y

    x=((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    y=((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))

    return Point(x,y)

def collinear(point1,point2,point3):
    x1=point1.x
    x2=point2.x
    x3=point3.x
    y1=point1.y
    y2=point2.y
    y3=point3.y

    return abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))<0.0001

def pointOnSegment(point,segment):
    test1=collinear(point,wall.init,wall.fin)
    fewinitx=min(wall.init.x,wall.fin.x)
    morinitx=max(wall.init.x,wall.fin.x)  
    fewinity=min(wall.init.y,wall.fin.y)
    morinity=max(wall.init.y,wall.fin.y)
