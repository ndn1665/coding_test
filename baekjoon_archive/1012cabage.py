import sys
sys.setrecursionlimit(100000)

# 상,하,좌,우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def DFS(x, y):
    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= -1 or nx >= N or ny <= -1 or ny >= M:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] == 0
            DFS(nx, ny)


T = int(input())
for _ in range(T):
    count = 0
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]

    # 행렬 생성
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    # 행렬의 모든 원소 탐색
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                DFS(i, j)
                count += 1
    print(count)