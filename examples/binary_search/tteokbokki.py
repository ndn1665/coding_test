count, inquire = map(int, input().split())#동빈이의 떡 갯수, 손님이 원하는 최소 떡의 길이
array = list(map(int, input().split()))#동빈이의 떡 갯수만큼 각 떡의 길이 입력

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end)//2
    for i in array:
        if i >= mid:
            total += i-mid
    if total < inquire:
        end = mid -1
    else:
        result = mid
        start = mid + 1
print(result)