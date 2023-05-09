import re

#\s+(?P<info>\w*)
p = re.compile(r'(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)\s+(?P<info>\w*)')
print(p.sub('\g<1>','park 010-7102-1665 chan here'))
