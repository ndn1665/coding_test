map_size = int(input())

gmmap = [[0 for _ in range(map_size)]for _ in range(map_size)]
gmmap[0][0] = 2#초기 뱀 위치 설정
gmmap[0][1],gmmap[0][2],gmmap[0][3],gmmap[0][4] =  1,1, 1, 1
arr = [(0,'r'),(8, 'd'),(10, 'd'),(11, 'd'),(13,'l')]

course = []
minus = 0

for i in range(1,len(arr)):
    for j in range(arr[i][0] - arr[i-1][0]):
        course.append(arr[i-1][1])
for i in range(100):
    course.append(arr[len(arr)-1][1])

head_x,head_y = 0,0 #뱀 머리의 위치 0,0으로 초기화
tail_x,tail_y = 0,0 # 꼬리 위치도 0,0으로 초기화

head_count = 0
tail_count = 0
dx = [-1,1,0,0] # udlr
dy = [0,0,-1,1] # udlr
dir = ['u','d','l','r']
while True:

    for i in range(4):
        if course[head_count] == dir[i]:
            head_x += dx[i]#head좌표 최신화
            head_y += dy[i]
            head_count += 1
    if head_x >=len(gmmap) or head_x <0 or head_y >=len(gmmap) or head_y < 0:
        break
    if gmmap[head_x][head_y] == 0:
        gmmap[head_x][head_y] += 2  # 머리 좌표 게임맵에 반영
        gmmap[tail_x][tail_y] = 0 #꼬리자르기
        for i in range(4):
            if course[tail_count] == dir[i]:
                tail_x += dx[i]#tail 좌표 최신화
                tail_y += dy[i]
                tail_count +=1
    elif gmmap[head_x][head_y] == 1:
        gmmap[head_x][head_y] += 2
    else:
        break

print(head_count)