n = int(input())
coordinates = list(map(int, input().split()))
coordinates.sort()

antenna_place = coordinates[n//2] if n%2 == 1 else coordinates[n//2 -1]

print(antenna_place)