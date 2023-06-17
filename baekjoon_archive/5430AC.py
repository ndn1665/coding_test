'''
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
'''
import sys
input = sys.stdin.readline

tc = int(input())

def rd(func, strlen, arr):
    target = 0
    dir = 1
    start = 0
    last = strlen - 1
    newarr = []
    
    for ea in func:
        if ea == 'R':
            dir *= (-1)
            if start == last:
                continue
            else:
                if dir < 0:
                    target = last
                else:
                    target = start
        else:
            if start > last:
                return "error"
            if dir>0:
                start +=1
                target = start
            else:
                last -= 1
                target = last
    if dir > 0:
        return arr[start:last+1]
    else:
        for i in range(last,start-1,-1):
            newarr.append(arr[i])
        return newarr


for _ in range(tc):
    func = input().rstrip()
    strlen = int(input().rstrip())
    arr = input().rstrip()
    if arr == '[]':
        arr = rd(func,0,list())
    else:
        arr = list(map(int,arr.strip('['']').split(',')))
    arr = rd(func, strlen, arr)
    if arr != 'error':
        print('['+','.join(str(x) for x in arr)+']')
    else:
        print(arr)

