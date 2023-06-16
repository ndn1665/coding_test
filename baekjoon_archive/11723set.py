import sys
input = sys.stdin.readline

s = set()
m = int(input().rstrip())

for _ in range(m):
    
    first = input().rstrip().split()
    if len(first) == 2:
        a,b = first
        b = int(b)
    else:
        a = first
    if a == 'add':
        s.add(b)
    if a == 'remove':
        s.discard(b)
    if a == 'check':
        if b in s:
            print(1)
        else:
            print(0)
    if a == 'toggle':
        if b in s:
            s.discard(b)
        else:
            s.add(b)
    if a == 'all':
        s = set([i+1 for i in range(20)])
    if a == 'empty':
        s = set()