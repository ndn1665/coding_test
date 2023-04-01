num = input()
array = [int(x) for x in num]
result = array[0]
for i in array[1:]:
    if i <=1:
        result += i
    else:
        result *= i

print(result)
