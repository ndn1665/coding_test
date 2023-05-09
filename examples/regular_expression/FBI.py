import re

array = []
p = re.compile('(FBI)')
count = 0
for i in range(5):
    if p.search(input()):
        array.append(i+1)
        count +=1
if count == 0:
    print("HE GOT AWAY!")

for i in array:
    print(i ,end=' ')


