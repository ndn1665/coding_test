def find_team(team,member):
    if team[member] != member:
        team[member] = find_team(team, team[member])
    return team[member]

def union_team(team,a,b):
    a = find_team(team,a)
    b = find_team(team,b)
    if a < b :
        team[b] = a
    else:
        team[a] = b

n,m = map(int,input().split())

team = [i for i in range(n+1)]

for _ in range(m):
    operate,a,b = map(int,input().split())
    if operate == 0:
        union_team(team,a,b)
    if operate == 1:
        a_team = find_team(team,a)
        b_team = find_team(team,b)
        if a_team == b_team:
            print('yes')
        else:
            print('no')

