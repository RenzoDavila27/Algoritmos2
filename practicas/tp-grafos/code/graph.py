import heapq #Para usar colas con prioridad


#Ejercicio 1
def CreateGraph(v, a):
    graph = {}
    for vert in v:
        graph[vert] = []
    for pairs in a:
        graph[pairs[0]].append(pairs[1])
        graph[pairs[1]].append(pairs[0])
    return graph

#Ejercicio 2
def existPath(graph, v1, v2):

    def searchPath(vertex):
        if v2 in graph[vertex]:
            return True
        else:
            vertsTraveled.append(vertex)
            for adjunt in graph[vertex]:
                if adjunt in vertsTraveled:
                    continue
                return searchPath(adjunt)
        return False
    
    if v1 == v2:
        return True
    vertsTraveled = []
    return searchPath(v1)

#Ejercicio 3
def isConnected(graph):

    if len(graph) == 0:
        return True
    
    vertsTraveled = set()
    firstVert = next(iter(graph.keys()))
    queue = [firstVert]

    while len(queue) != 0:
        vert = queue.pop()
        vertsTraveled.add(vert)

        for adjunt in graph[vert]:
            if adjunt not in vertsTraveled:
                queue.insert(0,adjunt)
    
    return len(vertsTraveled) == len(graph)
    
#Ejercicio 4
def isTree(graph):

    def isAcyclic(graph):
        
        def DFSMod(graph):

            def dfsTravel(v, f):
                visited.append(v)
                for adjunt in graph[v]:
                    if adjunt not in visited:
                        return dfsTravel(adjunt, v)
                    else:
                        if adjunt == f:
                            continue
                        return False #Se encontro ciclo
                return True
            
            visited = []
            firstVertex = next(iter(graph.keys()))

            return dfsTravel(firstVertex, None)

        return DFSMod(graph)
    
    return (isConnected(graph) and isAcyclic(graph))

#Ejercicio 5:
def isCompleted(graph): #Suponiendo que grafo completo no puede tener lazos
    for v in graph.keys():
        if set(graph[v]) != set(graph.keys()) - set([v]):
            return False
    return True

#Ejercicio 6
def convertTree(graph):

    def DFSMod(graph):

        def dfsTravel(v, f):
            visited.add(v)
            for adjunt in graph[v]:
                if adjunt not in visited:
                    if not dfsTravel(adjunt, v):
                        deletedEdges.append([v,adjunt])
                else:
                    if adjunt != f and [adjunt,v] not in deletedEdges:
                        deletedEdges.append([v,adjunt])
            return True
        
        visited = set()
        first = next(iter(graph.keys()))
        deletedEdges = []
        visited.add(first)
        dfsTravel(first, None)

        return deletedEdges

    return DFSMod(graph)

#Ejercicio 7
def countConnections(graph):

    def dfsTravel(v):
        visited.append(v)
        for adjunt in graph[v]:
            if adjunt not in visited:
                return dfsTravel(adjunt)
            else:
                continue

    visited = []
    compConexas = 0
    for v in graph.keys():
        if v not in visited:
            dfsTravel(v)
            compConexas +=1
    return compConexas

#Ejercicio 8
def convertToBFSTree(graph, v):

    newGraph = {}
    for vertex in graph.keys():
        newGraph[vertex] = []


    queue = [v]
    visited = set()
    visited.add(v)
    
    while len(queue) != 0:
        vert = queue.pop()
        for adjunt in graph[vert]:
            if adjunt not in visited:
                queue.insert(0, adjunt)
                visited.add(adjunt)
                newGraph[vert].append(adjunt)
                newGraph[adjunt].append(vert)
    
    return newGraph

#Ejercicio 9
def convertToDFSTree(graph, v):

    def DFSTravel(vertex):

        for adjunt in graph[vertex]:
            if adjunt not in visited:
                visited.add(adjunt)
                DFSTravel(adjunt)
                newGraph[vertex].append(adjunt)
                newGraph[adjunt].append(vertex)
            
    newGraph = {}
    for vert in graph.keys():
        newGraph[vert] = []

    visited = set()
    DFSTravel(v)
    return newGraph

#Ejercicio 10
def bestRoad(graph, v1, v2):

    def BFSMod(graph):

        padres = {v1 : None}
        queue = [v1]
        visited = set(queue)

        while len(queue) != 0:
            v = queue.pop()
            for adjunt in graph[v]:
                if adjunt not in visited:
                    visited.add(adjunt)
                    padres[adjunt] = v
                    queue.insert(0, adjunt)
                    if adjunt == v2:
                        return padres
        return []
    
    result = BFSMod(graph)

    if result == []:
        return []
    else:
        road = [v2]
        padre = result[v2]
        while padre != None:
            road.insert(0, padre)
            padre = result[padre]
        return road
    
#Ejercicio 14
def PRIM(graph):

    n = len(graph)
    AACM = [[0 for i in range(n)] for j in range(n)]
    t = {}
    V = set([0] + [t for t in range(1,n)])
    U = set([0])
    edgesAvaibles = [(0,c) for c in range(n)]

    while V != U:
        a = edgesAvaibles[0][0]
        b = edgesAvaibles[0][1]
        menor = max(graph[a])
        if menor == 0:
            return None
        
        bool = False

        
        for x,y in edgesAvaibles:
            if graph[x][y] < menor and graph[x][y] != 0:
                menor = graph[x][y]
                a = x
                b = y
        

        t[(a,b)] = menor
        
        for p in range(n):
            if (p,b) not in edgesAvaibles and p in V-U:
                edgesAvaibles.append((b,p))
                bool = True

        edgesAvaibles.remove(((a,b)))
        for i in range(n):
            try:
                edgesAvaibles.remove((i,b))
            except:
                continue

        if bool:
            U.add(b)
    
    for edge in t.keys():
        AACM[edge[0]][edge[1]] = t[edge]
        AACM[edge[1]][edge[0]] = t[edge]

    return AACM
    
#Ejercicio 15
def KRUSKAL(graph):

    def makeSet(x):
        return set([x])

    def findSet(x):
        return forest[x]
    
    def union(x,y):

        result = forest[x] | forest[y] 

        for element in result:
            forest[element] = result

    forest = {}
    edges = []
    n = len(graph)
    AACM = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        forest[i] = makeSet(i)

    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0 and (graph[j][i],j,i) not in edges:
                edges.append((graph[i][j],i,j))
            
    edges.sort(key=lambda x:x[0])
    
    for edge in edges:
        if findSet(edge[1]) != findSet(edge[2]):
            union(edge[1], edge[2])
            AACM[edge[1]][edge[2]] = edge[0]
            AACM[edge[2]][edge[1]] = edge[0]

    return AACM

#Ejercicio 21
def Dijkstra(graph, s, v):

    def relax(u,v):
        if distancia[v] > distancia[u] + graph[u][v]:
            distancia[v] = distancia[u] + graph[u][v]
            padres[v] = u
    
    def initRelax():
        for i in range(len(graph)):
            if i != s:
                distancia[i] = float('inf')
            else:
                distancia[i] = 0
            padres[i] = None

    padres = {}
    distancia = {}
    visited = set([s])
    initRelax()
    priorityQ = []
    heapq.heappush(priorityQ, (distancia[s],s))
    
    bool = False

    while len(priorityQ) > 0:
        u = heapq.heappop(priorityQ)
        print(u)
        visited.add(u[1])
        if u[1] == v:
            bool = True
            break

        for i in range(len(graph)):
            if graph[u[1]][i] != 0 and i not in visited:
                relax(u[1], i) 
                if not any(segundo == i for _, segundo in priorityQ):
                    heapq.heappush(priorityQ, (distancia[i], i))
            
    if not bool:
        return None
    
    padre = padres[v]
    finalRoad = [v]
    while padre != None:
        finalRoad = [padre] + finalRoad
        padre = padres[padre]
        

    return finalRoad









        
