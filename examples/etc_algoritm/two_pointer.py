#리스트에 담긴 데이터에 순차적으로 접근해야 할때 2,3,4,5,6,7번 데이터라고 접근하는 방식이 아닌
#2번부터 7번 데이터 같은 느낌

n = 5
m = 5
data = [1,2,3,2,5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end <n:
        interval_sum += data[end]
        end +=1

    if interval_sum == m:
        count +=1
    interval_sum -= data[start]

#정렬되어있는 두 리스트의 합집합
n,m = 3,4
a = [1,3,4]
b = [3,4,6,8]

result = [0]*(n+m)

i = 0
j = 0
k = 0

while i <n or j < m:
    if i<n and j < m :
        if a[i] < b[j]:
            result[k] = a[i]
            i +=1
        elif a[i]>b[j] :
            result[k] = b[j]
            j +=1
        else:
            

    k +=1

print(result)