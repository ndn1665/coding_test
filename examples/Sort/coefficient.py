array = [5, 4, 2, 5, 0, 3, 2]  # len = 7 max =5
count = [0] * (max(array) + 1)  # [0,0,0,0,0,0]

for i in range(len(array)):
    count[array[i]] += 1

print(count)
for i in range(len(count)):  # 6번 반복 i = 0,1,2,3,4,5
    for j in range(count[i]):  #
        print(i, end=' ')
