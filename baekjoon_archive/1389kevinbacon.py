INF = int(1e9)

n,m = map(int,input().split())

relation = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    relation[i][i] = 0
for _ in range(m):
    a,b = map(int,input().split())
    relation[a][b] = 1
    relation[b][a] = 1
    

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            relation[i][j] = min(relation[i][j], relation[i][k] + relation[k][j])

result = []
for i in range(1,n+1):
    result.append((i,sum(relation[i])))

answer = min(result, key= lambda x:(x[1],x[0]))
print(answer[0])
