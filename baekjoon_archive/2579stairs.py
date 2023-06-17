import sys
input = sys.stdin.readline

n = int(input())
stairs = [0]


for _ in range(n):
    stairs.append(int(input())) # 각 계단의 값 받음

move = [1,2] #한개씩 오르거나 두개씩 오르는 경우
now = 0 # 현위치

dp = [0 for _ in range(n+1)]  #시작점에서의 dp값

if n >=3:
    dp[1] = stairs[1]
    dp[2] = max(stairs[2] ,(stairs[2] + dp[1]))
    for i in range(3,n+1):
        dp[i] = max((stairs[i] + dp[i-2]),(stairs[i] + stairs[i-1] + dp[i-3]))
elif n ==2 :
    dp[1] = stairs[1]
    dp[2] = max(stairs[2] ,(stairs[2] + dp[1]))
elif n ==1 :
    dp[1] = stairs[1]
print(dp[n])
    
