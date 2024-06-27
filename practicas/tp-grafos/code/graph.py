
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





        
