sol = [0]*30000

sol[1] = 0
sol[2] = 1
sol[3] = 1
sol[5] = 1

def solution(n):

    if sol[n] != 0:
        return sol[n]
    else:
        sol[n] = solution(n-1) + 1
        if n%2 == 0:
            sol[n] =min(sol[n], 1 + solution(n//2))
        if n%3 == 0:
            sol[n] =min(sol[n], 1 + solution(n//3))
        if n%5 == 0:
            sol[n] =min(sol[n], 1 + solution(n//5))
        return sol[n]
print(solution(26))

"""
바텀업 방식
d = [0]*30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i%2 == 0:
        d[i] = min(d[i], d[i//2] +1)
    if i%3 == 0:
        d[i] = min(d[i], d[i//3] +1)
    if i%5 == 0:
        d[i] = min(d[i], d[i//5] +1)
print(d[26])
"""