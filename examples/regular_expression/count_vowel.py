import re
array = []
while True:
    a = input()
    if a == '#':
        break
    array.append(a)
count = 0
def vowel_count(match):
    global count
    count += 1
p = re.compile('a|e|i|o|u',re.I)
for i in array:
    p.sub(vowel_count,i)
    print(count)
    count = 0
