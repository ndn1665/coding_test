import re

sentence = input()
patern = input()
p = re.compile( '('+ patern + ')' )
count = 0
while sentence:

    m = p.search(sentence)
    if m == None:break
    start,end = m.span()
    sentence = sentence[end:]
    count +=1

print(count)
