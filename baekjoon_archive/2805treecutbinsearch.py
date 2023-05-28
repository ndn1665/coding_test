import sys
input = sys.stdin.readline
n,m = map(int,input().split())
trees = list(map(int, input().split()))
end = max(trees)
start = 1

def binsearch(start,end, target):
    answer = 0
    while start <= end:

        mid = (start + end) // 2
        result = sum([i-mid for i in trees if i-mid > 0])
        if result >= target:
            answer = mid
            start = mid + 1
        elif result< target:
            end = mid - 1
    return answer

print(binsearch(start, end, m))
