num = input()
array = [int(x) for x in num]
check = array[0]
count = 0
for i in range(len(num)-1):
    if array[i] == check and array[i+1] != check:
        count +=1

print(count)