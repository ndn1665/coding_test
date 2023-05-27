n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
targets = list(map(int,input().split()))

def binary_search(start,end,target):
    while (start<=end) :
        mid = (start + end) // 2
        if a[mid] < target:
            start = mid +1
        elif a[mid] > target:
            end = mid -1
        else:
            return True
        
    return False

start = 0
end = n-1

for target in targets:
    if binary_search(start, end, target):
        print('1')
    else:
        print('0')
