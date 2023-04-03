n,m = map(int, input().split())

bowl = list(map(int, input().split()))#1 3 2 3 2
array = [0]*11

for i in bowl:
    array[i] += 1
result = 0
for i in range(1,m+1):
    n -= array[i]
    result += array[i]*n

print(result)

