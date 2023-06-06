import heapq
import sys
input = sys.stdin.readline
def minus(num):
    num = -num
    return num


tc = int(input())#2
for _ in range(tc):
    calcs = int(input().rstrip())#7,9
    visited=[False]*calcs
    q = []
    p =[]
    I_count = 0
    D_count =0
    for i in range(calcs):
        cal,num = input().split()
        num = int(num)
        if cal == 'I':
            I_count +=1
            heapq.heappush(q,(num,i))
            heapq.heappush(p,(-num,i))
        if cal == 'D':
            D_count +=1
            if D_count>I_count:
                D_count = I_count
                continue
            else:
                if num <0 and not visited[q[0][1]]:
                    visited[heapq.heappop(q)[1]] = True
                elif num >0 and not visited[p[0][1]]:
                    visited[heapq.heappop(p)[1]] = True
            while q:
                if visited[q[0][1]]:
                    heapq.heappop(q)
                else:break
            while p:
                if visited[p[0][1]]:
                    heapq.heappop(p)
                else:break
                
    if len(q) == 0:
        print('EMPTY')
    else:
        print(-p[0][0], q[0][0])
