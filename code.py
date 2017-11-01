points=[]

def distance(point1,point2):
    return ((point1.x-point2.x)**2+(point1.y-point2.y)**2+(point1.z-point2.z)**2)**0.5
def intersect(line1,line2):
    x1=line1.initpoint.x
    x2=line1.finalpoint.x
    x3=line2.initpoint.x
    x4=line2.finalpoint.x

    y1=line1.initpoint.y
    y2=line1.finalpoint.y
    y3=line2.initpoint.y
    y4=line2.finalpoint.y

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

def pointOnWall(point,wall):
    test1=collinear(point,wall.initpoint,wall.finalpoint)
    fewinitx=min(wall.initpoint.x,wall.finalpoint.x)
    morinitx=max(wall.initpoint.x,wall.finalpoint.x)  
    fewinity=min(wall.initpoint.y,wall.finalpoint.y)
    morinity=max(wall.initpoint.y,wall.finalpoint.y)
    
    xtest=(fewinitx-0.0001<=point.x) and (point.x<=morinitx+0.0001)
    ytest=(fewinity-0.0001<=point.y) and (point.y<=morinity+0.0001)

    test2= xtest and ytest

    return test1 and test2
    
def dot(point1,point2):
    return point1.x*point2.x+point1.y*point2.y+point1.z*point2.z

def magnitude(point1):
    return (point1.x**2+point1.y**2+point1.z**2)**0.5

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
        dproduct=dot(vector1,vector2):
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
        


