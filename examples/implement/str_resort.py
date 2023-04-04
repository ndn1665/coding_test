input = "k1ka5cb7"
new_array = []
count = 0
for i in input:
    if 97<= ord(i) <= 122:
        new_array.append(ord(i))
    else:
        count += int(i)
new_array.sort()
for i in new_array:
    print(chr(i),end='')
print(count)