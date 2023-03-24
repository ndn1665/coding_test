#거슬러 줘야하는 돈이 N원인 경우 거슬러줘야할 동전의 최소 개수
# N = 500*x + 100*y + 50*z + 10*w

N = int(input())
count = 0
changes = [500, 100, 50, 10]

for change in changes:
    count += N//change
    N %= change
print(count)