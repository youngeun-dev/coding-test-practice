# https://www.acmicpc.net/problem/6603
# 로또
import sys
input = sys.stdin.readline


def DFS(answer, idx):
    if len(answer) == 6:
        print(* answer)
        return
    for i in range(idx, n):
        DFS(answer + [data[i]], i + 1)

while True:
    data = list(map(int, input().split()))
    n = data.pop(0)
    if not data:
        break
    DFS([], 0)
    print()
