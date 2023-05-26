n = int(input())
array = []
stack = []
answer = []
pre = [ i for i in range(n,0,-1)]
for _ in range(n):
    array.append(int(input()))
i = 0
while pre:
    
    poped = pre.pop()
    answer.append('+')
    if poped == array[i]:
        i+=1
        for j in range(len(stack)):
            poped = stack.pop()
            answer.append('-')
            if poped == array[i]:
                i+=1
            else:
                break
    stack.append(poped)

if i != n:
    print('NO')
else:
    for i in range(len(answer)):

        print(answer[i])