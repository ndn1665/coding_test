d = [0]*100

def fibo(n):
    if n == 1 or n == 2:
        return 1
    #d리스트에 계산한 값을 넣는다.
    if d[n] != 0:
        return d[n]
    d[n] = fibo(n-1) + fibo(n-2)
    return d[n]
print(fibo(55))