import numpy as np

#adj=np.zeros((6,6))
#adjacency matrix

#adj[0]=[0,1,0,1,0,0]
#adj[1]=[1,0,1,0,0,0]
#adj[2]=[0,1,0,1,1,1]
#adj[3]=[1,0,1,0,0,0]
#adj[4]=[0,0,1,0,0,1]
#adj[5]=[0,0,1,0,1,0]

def pathFind(adj,init,fin):
    numvertex=adj.shape[0]
    
    parent=[0 for k in range(numvertex)]

    vertices=[k for k in range(numvertex)]

    distances=[1e10*int(k!=init) for k in vertices]
    unvisited=[k for k in range(numvertex) if bool(distances[k])]
    current=init
    visited=[current]

    while fin in unvisited:
        for k in range(numvertex):
            if adj[current][k]!=0 and k in unvisited:
                tent=distances[current]+adj[current][k]
                if tent<distances[k]:
                    distances[k]=tent
                    parent[k]=current
        unsearched=[distances[k] for k in range(numvertex) if k in unvisited]
        miny=1e5
        for k in range(numvertex):
            if distances[k]<miny and k in unvisited:
                miny=distances[k]
                mink=k
        new=mink
        try:       
            unvisited.remove(new)
        except:
            print(unvisited)
            print(new)
        current=new
        visited.append(current)       

    search=fin
    result=[]
    while search!=init:
        result.append(search)
        search=parent[search]
    result.append(init)
    result=result[::-1]
    return result 

