
def find_village(village,house):
    if village[house] != house:
        village[house] = find_village(village,village[house])
    return village[house]

def union_village(village,a,b):
    a = find_village(village,a)
    b = find_village(village,b)
    if a<b:
        village[b] = a
    else:
        village[a] = b

house, road = map(int,input().split())

village = [i for i in range(house + 1)]

all = []

for _ in range(road):
    a,b,cost = map(int,input().split())
    all.append((cost,a,b))

all.sort()
result = []
for each in all:
    cost,a,b = each
    if find_village(village,a) == find_village(village,b):
        continue
    else:
        union_village(village,a,b)
        result.append(cost)

print(sum(result[:-1]))
 