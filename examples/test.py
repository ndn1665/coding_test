num = 3
d = [(0,0) for _ in range(num+1)]
d[0] = (1,0)
d[1] = (0,1)
for i in range(2,num+1):
    d[i] = ((d[i-1][0] + d[i-2][0]),(d[i-1][1] + d[i-2][1]))

print(d)