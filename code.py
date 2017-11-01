
class Point:
    def __init__(self,xpos,ypos,clas="House"):
        self.x=xpos
        self.y=ypos
        self.location=(xpos,ypos)
        self.clas=clas
    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Point(self.x-other.x,self.y-other.y)
    def __str__(self):
        return str(self.location)
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    def __repr__(self):
        return str(self)
        
    def dot(self,other):
        return self.x*other.x+self.y*other.y

class Segment:
    def __init__(self,Point1,Point2):
        self.init=Point1
        self.fin=Point2
    def __eq__(self,other):
        if self.init==other.fin:
            return self.fin==other.init
        else:
            return self.init==other.init and self.fin==other.fin
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

houses=[Point(0,1),Point(-1,1),Point(-2,1),Point(0,0),Point(1,0),Point(2,0),Point(0,-1),Point(1,-1),Point(2,-1)]
stores=[Point(5,1),Point(4,4),Point(0,6)]
offices=[Point(2,8),(5,8),(7,4)]

roads=[Segment(Point(0,-1),Point(3,-1)),Segment(Point(-3,1),Point(5,1)),Segment(Point(0,-1),Point(-0,6)),Segment(Point(4,1),Point(4,4)),Segment(Point(0,4),Point(7,4)),Segment(Point(2,4),Point(2,8)),Segment(Point(2,8),Point(5,8)),Segment(Point(5,4),Point(5,8))]

intersections=[]

for k in range(len(roads))
    for i in range(len(roads))
        if i!=k:
            try:
                intsect=intersect(roads[i],roads[k])
                intersections.append(intsect)
            except:
                pass

print(roads)


path=[]

for k in range(len(points)):
    for j in points[k].roads:
        result=[]
        minDist=1e5
        for i in range(len(points)):
            if i!=k:
                test1=PointOnLine(points[i],j)
                if test1:
                    dist=distance(points[i],points[k])
                    if dist<minDist:
                        temp=minDist
                        tempI=minI
                        minDist=dist
                        minI=i
        vector1=point[minI]-points[k]
        vector2=point[tempI]-points[k]
        dproduct=vector1.dot(vector2)
        adj[k][minI]=minDist
        if dproduct<0:
            adj[k][tempI]=temp
yresult=[]
xresult=[]
for k in range(len(path)-1):
    if close(points[path[k]].x,points[path[k+1]].x):
        yarray=np.linspace(points[path[k]].y,points[path[k+1]].y)
        xarray=np.full(50,points[path[k]].x)
    else:
        xarray=np.linspace(points[path[k]].x,points[path[k+1]].x)
        yarray=np.full(50,points[path[k]].y)
    for element in xarray:
        xresult.append(element)
    for element in yarray:
        yresult.append(element)
