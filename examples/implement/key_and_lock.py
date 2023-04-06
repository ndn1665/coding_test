def rotate(arr):#1회전 후 회전 된 배열을 반환하는 함수
    line = len(arr)  # 행의 크기 3
    row = len(arr[0])  # 열의 크기 3
    new_arr = [[0 for _ in range(line)] for _ in range(row)]
    for i in range(line):
        for j in range(row):
            new_arr[j][row - (i + 1)] = arr[i][j]
    return new_arr

key =  [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]

key_wide = [[0 for _ in range(9)]for _ in range(9)]


lock_wide= [[0 for _ in range(9)]for _ in range(9)]
for i in range(3):
    for j in range(3):
        lock_wide[i+3][j+3] = lock[i][j]


def compare(key_wide, lock_wide):
    for i in range(3):
        for j in range(3):
            lock_wide[i+3][j+3] += key_wide[i+3][j+3] # lock_wide에 key_wide 대입
            if lock_wide[i+3][j+3]  == 2: # 둘다 돌기면 false 반환
                return False
    for i in range(3):
        for j in range(3):
            if lock_wide[i+3][j+3] == 0: # lock을 풀 지 못했으면 false 반환
                return False
    return True # 딱 맞으면 True 반환



#def solution(key, lock):
#    answer = True

#    return answer
for i in range(9):
    print(lock_wide[i])