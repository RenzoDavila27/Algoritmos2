
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
                queue.append(adjunt)
    
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








        
