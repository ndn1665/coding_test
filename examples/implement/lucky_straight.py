n = int(input())#123402
new_n = str(n)#'123402'
length = len(new_n)#6
front = 0
back = 0
for i in range(length//2):
    front += int(new_n[i])
    back += int(new_n[-(i+1)])

if front == back:
    print('lucky')
else:
    print("ready")