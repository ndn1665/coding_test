## 이건 내 풀이
N, M, K = map(int, input().split())  # 배열의 크기 N, 숫자가 더해지는 횟수 M, 연속 합 제한 K

nums = list(map(int, input().split()))  # N 입력됨

#
# 큰수의 법칙 구현
#
result = 0
maxnum = max(nums)
count = nums.count(maxnum)
if count >= 2:
    result = M * maxnum
else:
    nums.remove(maxnum)
    second = max(nums)
    first_part = M // (K + 1)
    rest_part = M % (K + 1)

    result = first_part * (maxnum * K + second) + rest_part * maxnum

print(result)