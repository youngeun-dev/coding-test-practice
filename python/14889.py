# https://www.acmicpc.net/problem/14889
# 스타트 링크
import sys
input = sys.stdin.readline


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
people = []
def power():
    team1 = 0
    team2 = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if visited[i] and visited[j]:
                team1 += graph[i][j]
                team1 += graph[j][i]
            elif not visited[i] and not visited[j]:
                team2 += graph[i][j]
                team2 += graph[j][i]

    return abs(team1 - team2)


answer = sys.maxsize
def dfs(depth, idx, n):
    global answer
    if depth == n // 2:
        answer = min(answer, power())
        if answer == 0: # 0이면 프로그램 종료
            print(answer)
            exit()
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            dfs(depth + 1, i + 1, n)
            visited[i] = 0


dfs(0, 0, n)
print(answer)
