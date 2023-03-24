A = []
B = []
# 두 배열읜 N개의 원소로 구성,원소는 모두 자연수
#최대 k 번의 바꿔치기 연산 을 수행(배열A의 원소 하나와 배열 B의 원소 하나를 골라서 두 원소를 서로 바꾸는 것)

#배열 A의 원소의 합이 최대가 대야함

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

for i in range(k):
    if a[i] < b[i]:
        a[i],b[i] = b[i],a[i]

print(sum(a))