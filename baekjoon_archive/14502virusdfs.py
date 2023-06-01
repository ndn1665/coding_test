'''
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

9
'''
import itertools
import copy
from collections import deque

INF = int(1e9)
n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]



def dfs(nmap,i,j):
    if i < 0 or i>=n or j<0 or j>=m:
        return False
    if nmap[i][j] == 1 or visited[i][j]:
        return False
    visited[i][j] = True
    if nmap[i][j] == 0:
        nmap[i][j] = 2
    dfs(nmap,i-1,j)
    dfs(nmap,i+1,j)
    dfs(nmap,i,j-1)
    dfs(nmap,i,j+1)
    return True


selection = [] 
for i in range(n):#selection list에 벽을 설치할 수 있는 좌표를 튜플형태로 하나씩 저장한다.
    for j in range(m):
        if maps[i][j] != 0:
            continue
        selection.append((i,j))
answer = INF

three_picks = list(itertools.combinations(selection,3)) 
#selection에서 3개의 조합,즉 3개의 좌표가 될 수 있는
#후보군들을 ((1좌표),(2좌표),(3좌표))의 형태로 리스트로만든다
max = 0
for three_pick in three_picks: #좌표군들 중 한 경우 선택
    nmap = copy.deepcopy(maps)
    visited = [[False] * (m) for _ in range(n)]
    result = 0
    
    for pick in three_pick:
        nmap[pick[0]][pick[1]] = 1 #nmap에 벽 설치
    
    for i in range(n):
        for j in range(m):
            if nmap[i][j] == 2:
                dfs(nmap,i,j)
    for i in range(n):
        result += nmap[i].count(0)
    if max < result:
        max = result
print(max)