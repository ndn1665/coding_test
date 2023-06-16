import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int,input().split()))

sasarray = sorted(set(array))

dic = {}
for i in range(len(sasarray)):
    dic[sasarray[i]] = i


for i in array:
    print(dic[i],end=' ')