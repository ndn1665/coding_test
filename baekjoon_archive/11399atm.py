n =int(input())
array = list(map(int,input().split()))

array.sort(reverse=True)
result = 0
for i in range(n):
    result +=sum(array[i:n])
print(result)