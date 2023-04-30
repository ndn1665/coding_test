#bisect는 이진탐색알고리즘을 구현한 모듈
#bisect에 있는 left와 right메서드는 정렬된 리스트에 값을 삽입할 때 정렬을 유지할 수 있는 인덱스를 반환
#ex>

from bisect import bisect_left, bisect_right
a = [1,2,4,4,8]
print(bisect_left(a,2))
print(bisect_right(a,4))

#find_num_count_in_sort를 bisect를 활용해서 풀기

def count_by_range(array, left,right):
    right_index = bisect_right(array,right)
    left_index = bisect_left(array, left)
    return right_index - left_index

n,target = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array,target,target)

if count == 0:
    print(-1)
else:
    print(count)