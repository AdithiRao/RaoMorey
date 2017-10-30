points=[]

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
        


