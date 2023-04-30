import sys
input = sys.stdin.readline
n = int(input())
students = []
for i in range(n):
    name,kor,eng,math = input().split()
    students.append((name,int(kor),int(eng),int(math)))

#파이썬에서는 튜플을 원소로 하는 리스트를 정렬하면, 각 튜플을 구성하는 원소의 순서에 맞게 정렬됨

students.sort(key = lambda x:( (-x[1]),(x[2]),(-x[3]),(x[0]) ) )
for student in students:
    print(student[0])
