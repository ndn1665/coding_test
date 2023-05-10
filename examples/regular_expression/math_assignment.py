import re

n = int(input())
p = re.compile('[0-9]+')

answer = []
for _ in range(n):
    result = p.findall(input())
    for x in result:
        answer.append(int(x))
answer.sort()
for i in range(len(answer)):
    print(answer[i])

