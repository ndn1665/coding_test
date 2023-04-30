import sys
input = sys.stdin.readline
n,target = map(int, input().strip().split())
array = list(map(int,input().strip().split()))

def first(array,target,start,end):
    while (start<=end):
        mid = (start + end) // 2
        if array[mid] == target and (mid == 0 or array[mid-1] < target):
            return mid
        elif array[mid] >= target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
    if start > end:
        return None
def last(array, target,start,end):
    while (start<=end):
        mid = (start + end) // 2
        if array[mid] == target and (array[mid + 1] > target or mid == n-1):
            return mid
        elif array[mid] <= target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
    if start > end:
        return None

print(last(array, target, 0, n-1) - first(array, target, 0, n-1) + 1)
