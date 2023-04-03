import sys
input=sys.stdin.readline
#k//length보다 작은 애들은 무시
food_times = list(map(int, input().split()))
k = int(input())

def solution(food_times, k):

    length = len(food_times)
    count = [x + 1 for x in range(length)]
    answer = 0
    cutline = k // length
    rest = k%length

    new_array = []
    for i in range(length):
        if food_times[i] > cutline:
            new_array.append(food_times[i])
    final = rest%len(new_array)#0
    answer =  count[food_times.index(new_array[final])]#
    return answer

print(solution(food_times, k))