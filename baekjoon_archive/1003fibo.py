tc = int(input())
array = [int(input()) for _ in range(tc)]

def dp(num):
    d = [(0,0) for _ in range(num+1)]
    d[0] = (1,0)
    if num == 0:
        return d[0]
    d[1] = (0,1)
    for i in range(2,num+1):
        d[i] = ((d[i-1][0] + d[i-2][0]),(d[i-1][1] + d[i-2][1]))

    return d[num]

for num in array:
    print(dp(num)[0],dp(num)[1])




