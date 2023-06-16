import sys
input = sys.stdin.readline

def findparent(parent,x):
    if parent[x] != x:
        parent[x] = findparent(parent, parent[x])
    return parent[x]


def unionparent(parent,a,b):
    a = findparent(parent,a)
    b = findparent(parent,b)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a

v,e = map(int,input().split())
parent = [i for i in range(v+1)]
for _ in range(e):
    a,b = map(int,input().split())
    unionparent(parent,a,b)

for i in range(1,v+1):
    findparent(parent,i)
s = set(parent[1:])
count = 0
for i in s:
    count +=1
print(count)