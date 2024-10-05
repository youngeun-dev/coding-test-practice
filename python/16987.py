# https://www.acmicpc.net/problem/16987
# 계란으로 계란치기
import sys
input = sys.stdin.readline


def backTracking(start):
    global result
    if start == n: # 맨 마지막 계란까지 탐색한 경우
        count = 0
        for i in range(n):
            if egg[i][0] <= 0:
                count += 1
        result = max(result, count)
        return

    if egg[start][0] <= 0: # 계란을 깰 수 없는 경우
        backTracking(start + 1)
        return

    check = True # 모두 깨졌는 지 확인
    for i in range(n):
        if i == start:
            continue
        if egg[i][0] > 0:
            check = False
            break

    if check:
        result = max(result, n - 1)
        return

    for i in range(n):
        if start != i and egg[i][0] > 0:
            egg[start][0] -= egg[i][1]
            egg[i][0] -= egg[start][1]
            backTracking(start + 1)
            egg[start][0] += egg[i][1]
            egg[i][0] += egg[start][1]


n = int(input())
egg = [list(map(int, input().split())) for _ in range(n)]
result = 0

backTracking(0)
print(result)


# ---------------------------------------------
import sys
input = sys.stdin.readline

def check_broke(eggs):
    cnt = 0
    for egg in eggs:
        if egg[0] <= 0:
            cnt += 1

    return cnt


def back_tracking(start):
    global result
    cnt = check_broke(eggs)
    result = max(cnt, result)
    if result == n or start == n:
        return result

    if eggs[start][0] <= 0:
        back_tracking(start + 1)
        return

    for nxt_egg in range(n):
        if start != nxt_egg and eggs[nxt_egg][0] > 0:
            eggs[start][0] -= eggs[nxt_egg][1]
            eggs[nxt_egg][0] -= eggs[start][1]
            back_tracking(start + 1)
            eggs[start][0] += eggs[nxt_egg][1]
            eggs[nxt_egg][0] += eggs[start][1]


n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)] # [내구도, 무게]
result = 0
back_tracking(0)
print(result)
