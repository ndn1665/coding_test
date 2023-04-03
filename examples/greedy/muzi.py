food_times = list(map(int, input().split()))
k = int(input())

def solution(food_times, k):

    length = len(food_times)
    count = [x + 1 for x in range(length)]
    answer = 0
    cnt = 0
    i = 0
    while True:
        i %= length
        if food_times[i]:
            food_times[i] -= 1
            cnt += 1

        if cnt == k:
            while True:

                if food_times[i]:
                    answer = count[i]
                    return answer
                else:
                    i += 1
                i %= length
        i += 1

result = solution(food_times,k)
print(result)

