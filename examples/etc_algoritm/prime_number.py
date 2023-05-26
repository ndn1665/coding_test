import math

def is_prime_number(x):
    for i in range(2,int(math.sqrt(x)) + 1):#중간 약수까지만 test하면 됨
        if x %i == 0:
            return False
    return True

# 중간 약수까지만 하는 이유는 16의 약수는 1 2 4 8 16 이고 1과 16은 곱해서 16, 2와 8은 곱해서 16 이므로 중간까지만 테스트하면 전부를
# 테스트 한것이 됨
