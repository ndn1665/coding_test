#heapq 알고리즘을 써야함 원리는 내가 작성한 코드랑 동일한데 시간초과가 뜸
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
m = n

array = []
for i in range(n):
    array.append( int( input() ) )
result = 0
while True:
    if len(array) == 1:
        break
    array.sort(reverse=True)
    a = array.pop()
    b = array.pop()
    result += a+b
    array.append(result)

print(result)

