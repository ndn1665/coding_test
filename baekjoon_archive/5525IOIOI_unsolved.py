import re
import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
s = input().rstrip()

pattern = "IO"*(n)+"I"
patternLen = len(pattern)
count = 0
for i in range(len(s)):
    if i+patternLen > len(s):
        break
    if s[i:i+patternLen] == pattern:
        count +=1
    
print(count)
#위풀이는 50점짜리풀이고 아래풀이가 100점임 ㅜㅜ
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
