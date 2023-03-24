graph = [[],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7] ]

def dfs(graph, v, visited):
    visited[v] = True # 현재 노드 v는 방문 처리
    print(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False]*9

dfs(graph, 1, visited)