
def dfs(start, graf):
    vertexList, reletiveList = graf
    adjacentList = [[] for _ in  vertexList]
    for reletive in reletiveList:
        adjacentList[reletive[0]].append(reletive[1])
    stack = [start]
    visitList = []
    while stack :
        cur = stack.pop()
        for adj in adjacentList[cur]:
            if adj not in visitList:
                stack.append(adj)
        visitList.append(cur)

    return visitList

vertexList = [0,1,2,3,4,5,6,7,8]
reletivelist = [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6),(4,7),(7,8)]
graf = (vertexList, reletivelist)
start = 0
print dfs(start, graf)
