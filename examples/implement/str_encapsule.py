arr= "ababcdcdababcdcd"
def solution(s):
    answer = len(s)

    for loop in range(1, (len(s) // 2) + 1):  # 1,2,3,4,5,6
        count = 1
        i = 0
        new = 0

        while True:

            if s[i:i + loop] == s[i + loop:i + (loop * 2)]:
                count += 1
                i += loop
                continue
            if count > 1:  # 한번이라도 반복이면
                new = new + 1 + len(s[i:i + loop])
            elif count == 1:  # 한번도 반복이 아니면
                new = new + len(s[i:i + loop])
            count = 1
            i += loop
            if i >= len(s):
                break
        if answer > new:
            answer = new
    return answer

print(solution(arr))

