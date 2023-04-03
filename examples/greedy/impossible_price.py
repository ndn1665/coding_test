n = int(input())
m = list(map(int, input().split()))
m.sort()

target = 1

for i in m:
    if target < i:#i가 target보다 같거나( 같으면 target값을 그냥 만들 수 있으므로, 작아야 (작으면 0이 아니므로 최소 i는 1 일테고 target은
                    #이미 만들 수 있는 금액 + 1 이 target이므로 i값을 이미 만들 수 있는 금액리스트에 더하면 target을 충족하게 된다
                    # 그러므로 target값을 업데이트 할 수 있다.
        break
    target += i
print(target)