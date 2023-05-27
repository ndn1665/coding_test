from collections import deque
import sys
input = sys.stdin.readline
n = int(input().rstrip())
q = deque()
for i in range(n):
    q.append(i+1)

while len(q) > 1:
    q.popleft()
    go_to_last = q.popleft()
    q.append(go_to_last)

print(q.popleft())
