
n = int(input())
array = []

for _ in range(n):
    a,b = map(int, input().split())
    array.append((a,b))

array.sort(key = lambda x: (x[1],x[0]))
result = []
result.append(array[0])
count = 0
for i in range(1,len(array)):
    if array[i][0]>= result[count][1]:
        result.append(array[i])
        count +=1
print(len(result))