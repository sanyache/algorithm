
def bfs(start, graf):
    vertexList, reletivelist = graf
    adjList = [[]for _ in vertexList]
    for reletive in reletivelist:
        adjList[reletive[0]].append(reletive[1])
    queue = [start]
    visitList = []
    while queue:
        cur = queue.pop()
        for adj in adjList[cur]:
            if adj not in visitList:
                queue.insert(0,adj)
        visitList.append(cur)
    return visitList

vertexList = [0,1,2,3,4,5,6,7,8]
reletivelist = [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6),(4,7),(7,8)]
graf = (vertexList, reletivelist)
start = 0
print bfs(start, graf)