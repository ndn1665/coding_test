import re
sentence = input()
p = re.compile(r'dz=|[ln]j|\w\W')
print(p.findall(sentence))
