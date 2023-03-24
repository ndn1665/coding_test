num = int(input())
array = []
for i in range(num):
    (name, score) = input().split()
    array.append((name, score))

array = sorted(array, key=lambda x: int(x[1]))
for i in range(num):
    print(array[i][0], end=' ')