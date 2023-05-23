#find_parent 부분 수정
#부모테이블을 바로 루트테이블로 초기화
def find_parent(parent,x):
    if parent[x] != x:
       parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int, input().split())
parent = [0] *(v+1)

for i in range(1,v+1):
    parent[i] = i

for i in range(e):
    a,b = map(int, input().split())
    union_parent(parent,a,b)

print('the set of each item : ',end = ' ')
for i in range(1,v+1):
    print(find_parent(parent,i),end = ' ')

print()

print('parent table : ',end = '')
for i in range(1,v+1):
    print(parent[i] ,end = ' ')
