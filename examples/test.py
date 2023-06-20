import re
import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
s = input().rstrip()
i =0
count = 0
answer =0
while True:
    if i+3 > m:
        break
    if s[i:i+3] == "IOI":
        count +=1
        i+=2
        if count == n:
            answer +=1
            count -=1
    else:
        count = 0
        i+=1
print(answer)
