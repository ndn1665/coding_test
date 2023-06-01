#해시테이블을 이용한 풀이
n,m = map(int, input().split())
dictionary = {}
people = []
result = 0
for _ in range(n):
    person = input()
    dictionary[person] = 1
for _ in range(m):
    person = input()
    if person in dictionary:
        result +=1
        people.append(person)

people.sort()

print(result)
for i in people:
    print(i)
#집합 자료형을 이용한 풀이
#교집합 사용
a = set()
for _ in range(n):
    a.add(input())
b = set()
for _ in range(m):
    b.add(input())

result = sorted(list(a&b))#교집합
print(len(result))
