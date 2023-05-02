import sys
input = sys.stdin.readline

n,wifi = map(int,input().split())
array = [int(input()) for i in range(n)]
array.sort()
start,end = 1, array[n-1] - array[0]
# 집 사이의 최소 거리, 최대 거리
result = 0

if wifi == 2:
    print(array[n-1] - array[0])
    # 집이 2개라면 무조건 처음, 마지막 집 사이의 거리
else:
    while (start<=end):
        mid = (start + end) // 2
        count = 1
        latest = array[0]
        for i in range(n):
            if array[i] - latest >= mid:
                latest = array[i]
                count +=1
        if count < wifi:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    print(result)