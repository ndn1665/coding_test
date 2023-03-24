num = int(input())
array = []
for i in range(3):
    array.append(int(input()))

array = sorted(array, reverse=True)
print(array)