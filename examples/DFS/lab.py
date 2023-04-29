n,m = map(int, input().split())
lab = [

       [2,0,0,0,1,1,0],
       [0,0,1,0,1,2,0],
       [0,1,1,0,1,0,0],
       [0,1,0,0,0,0,0],
       [0,0,0,0,0,1,1],
       [0,1,0,0,0,0,0],
       [0,1,0,0,0,0,0]

       ]
maximum = 0
wall_count = 3 # 주어진 벽 3개

for line in lab:# wall 수 count 하기
    wall_count += line.count(1)

def check():#dfs한 map에있는 안전한 방의 수
def dfs(x,y):#2의 수 count
    if x<= -1 or x>=n or y<= -1 or y>= m :
        return False

for i in range(n):
    for j in range(m):
        if check() > maximum:
