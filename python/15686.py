import sys
input = sys.stdin.readline

n, m = map(int, input().split())

house = []
chicken = []

for x in range(n):
    row = list(map(int, input().split()))
    for y in range(n):
        if row[y] == 1:
            house.append((x + 1, y + 1))
        elif row[y] == 2:
            chicken.append((x + 1, y + 1))

answer = 1e9
temp = []

def chicken_distance(idx):
    global answer
    if len(temp) == m:
        distance = 0
        for r1, c1 in house:
            d = 1e9
            for r2, c2 in temp:
                d = min(d, abs(r1 - r2) + abs(c1 - c2))
            distance += d
        answer = min(answer, distance)
        return

    for i in range(idx, len(chicken)):
        temp.append(chicken[i])
        chicken_distance(i + 1)
        temp.pop()


chicken_distance(0)
print(answer)
