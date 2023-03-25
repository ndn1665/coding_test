count, inquire = map(int, input().split())#동빈이의 떡 갯수, 손님이 원하는 최소 떡의 길이
array = list(map(int, input().split()))#동빈이의 떡 갯수만큼 각 떡의 길이 입력
array.sort()


def binary_search(inquire,array,start,end):
    result = cut(array)#제일 처음 상황에서 잘라주기
    if result == inquire:
        return array[0]

    mid = (start + end)//2

    array = array[mid:]

    if result > inquire:
        start = mid
        return binary_search(inquire,array, start, end)
    if result < inquire:
        start = (mid +start)//2
        return binary_search(inquire, array, start, end)


def cut(array):
    cutter = array[0]
    result = 0
    for i in array:
        result += (i - cutter)
    return result

print(binary_search(inquire,array,0,count-1))