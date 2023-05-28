n = int(input())

array = []#4 3 6 8 7 5 2 1
answer = []
for _ in range(n):
    array.append(int(input()))
stack = []
pre = [i for i in range(n,0,-1)]
i = 0
while pre:
    poped = pre.pop()
    stack.append(poped)
    answer.append('+')
    if poped == array[i]:
        stack.pop()
        answer.append('-')
        i+=1
        while  stack:
            poped = stack.pop()
            if poped == array[i]:
                answer.append('-')
                i+=1
            else:
                stack.append(poped)
                break

if i == n:
    for i in answer:
        print(i)
else:
    print('NO')