# ascii 97 == a

result_x = [chr(97 + i) for i in range(8)]
result_y = [1 + i for i in range(8)]

x = int(input())
y = int(input())

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

count = 0

for i in range(8):
    nx = 0
    ny = 0

    nx = x + dx[i]
    ny = y + dy[i]
    if nx <= 0 or ny <= 0 or nx >= 9 or ny >= 9:
        continue
    else:
        count += 1

print(count)