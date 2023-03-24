line, row = map(int, input().split())

result = 0

for i in range(line):
    array = list(map(int, input().split()))
    min_num = min(array)
    result = max(result, min_num)
print(result)