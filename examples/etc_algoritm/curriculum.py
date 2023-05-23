from collections import deque
from copy import deepcopy

stage = int(input())

courses = [[] for _ in range(stage + 1)]
times = [0 for _ in range(stage + 1)]
indegree = [0 for _ in range(stage + 1)]
for i in range(1,stage+1):
    course = list(map(int, input().split()))
    times[i]= course[0]
    if len(course[1:-1]) > 0:
        for ea in course[1:-1]:
            courses[ea].append(i)
            indegree[i]+= 1

print(courses)
print(times)
print(indegree)
result = deepcopy(times)
def topology_sort():
    
    q = deque()
    for i in range(1,stage+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in courses[now]:
            result[i] = max(result[i] , result[now] + times[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
topology_sort()
print(result)