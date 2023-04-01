n = int(input())
array = list(map(int,input().split()))
array.sort(reverse=True)
team_count = 0
j = 0
while True:
    if j == n:
        break
    for i in range(array[j]):
        j += 1
    team_count +=1

print(team_count)