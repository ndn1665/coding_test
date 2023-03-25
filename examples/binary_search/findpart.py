n = int(input())#5
n_array = list(map(int, input().split()))#8 3 7 9 2
n_array.sort()
m = int(input())#3
m_array = list(map(int, input().split()))# 5 7 9
m_array.sort()

def search(array, target, start, end):
    if start > end:
        return "no"
    mid = (start + end)//2 #중간값의 좌표
    if target == array[mid]:
        return "yes"
    elif array[mid] > target:
        return search(array, target, start, mid-1)
    elif array[mid] < target:
        return search(array, target, mid+1, end)

for i in m_array:
    print(search(n_array, i, 0, n-1))
