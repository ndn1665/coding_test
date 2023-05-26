def combination(n,r):
    if (n == r or r == 0):
        return 1
    else:
        return combination(n-1,r-1) + combination(n, r-1)