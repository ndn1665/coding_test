## 그리디 하게 풀기
N, M, K = map(int, input().split())  # 배열의 크기 N, 숫자가 더해지는 횟수 M, 연속 합 제한 K

nums = list(map(int, input().split()))  # N 입력됨

nums.sort()

first = nums[N - 1]
second = nums[N - 2]
result = 0
while True:

    for i in range(K):
        if M == 0: break
        result += first
        M -= 1
    if M == 0: break
    result += second
    M -= 1

print(result)