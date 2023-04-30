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
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)

# end = mid - 1 과 start = mid + 1 을 해줘야 한다 왜냐면 while (start <= end)일때 반복하는 반복문에서 end = mid 고 start = mid인
#상황이 오면 무한루프에 빠진다. 그래서 while (start <= end)루프일때 end = mid - 1 start = mid + 1을 하면 탈출 할 수 있다.그리고 시작값이
# 예를 들어 mid(14)에서 +1된 15여도 end 가 15까지 접근할 수 있기 때문에, mid가 15가 되는 상황이 안나올것을 걱정하지 않아도 된다.