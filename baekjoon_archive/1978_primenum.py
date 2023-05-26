import math
n =int(input())
array = list(map(int,input().split()))

def find_sosu(num):
    number = int(math.sqrt(num))
    for i in range(2,number + 1):
        if num % i == 0:
            return False
    return True
result = 0
for num in array:
    if find_sosu(num) and num != 1 :
        result +=1
print(result)
