# https://www.acmicpc.net/problem/20006
# 랭킹전 대기열
import sys
input = sys.stdin.readline

# p: 플레이어의 수
# m: 방의 정원
# n: 플레이어의 닉네임
# l: 플레이어의 레벨
p, m = map(int, input().split())
player = []
for _ in range(p):
    l, n = map(str, input().split())
    player.append([int(l), n])

rooms = []
for level, nickname in player:
    join = False # 입장 했는지 확인
    for i in range(len(rooms)):
        if len(rooms[i][1]) == m: # 정원이 꽉찬 경우
            continue
        if rooms[i][0] - 10 <= level <= rooms[i][0] + 10: # 입장이 가능한 경우
            join = True
            rooms[i][1].append([level, nickname])
            break
    if not join: # 입장 가능한 방이 없음 -> 방 만들기
        rooms.append([level, [[level, nickname]]])

for room in rooms:
    room[1].sort(key=lambda x: x[1]) # 닉네임 순 출력
    print("Started!" if len(room[1]) == m else "Waiting!")
    for x, y in room[1]:
        print(x, y)
