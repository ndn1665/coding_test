from collections import Counter

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

array.sort()
length = len(array)

def sansul(array):
    result = 0
    for i in array:
        result += i
    return int(round(result / length,0))

def center(array):
    mid = length // 2
    return array[mid]


def most(array):
    array.sort()
    str_arr = list(map(str, array))

    counted = Counter(str_arr)
    max_count = max(counted.items(), key=lambda x : x[1])

    answer_arr = [i for i in counted.items() if i[1] == max_count[1]]

    if len(answer_arr) == 1:
        return (answer_arr[0][0])
    else:

      return    (answer_arr[1][0])
def ranger(array):
    return max(array) - min(array)

print(sansul(array))
print(center(array))
print(most(array))
print(ranger(array))


