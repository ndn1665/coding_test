
k,n= map(int,input().split())
array = []
for i in range(k):
    array.append(int(input()))

array.sort()
def binary_search(start, end,n):
    answer = 0
    while (start <= end):
        mid = (start + end)//2
        new_array = [i//mid for i in array]
        result = sum(new_array)
        
        if result < n :
            end = mid - 1
        elif result >= n:
            answer = mid
            start = mid + 1
    return answer
        
print(binary_search(1,array[k-1],n))