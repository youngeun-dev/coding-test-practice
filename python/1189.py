# https://www.acmicpc.net/problem/1189
# 컴백홈
import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
graph = [list(input()) for _ in range(r)]
graph[r - 1][0] = 'T' # 시작 지점

end = (0, c - 1)
answer = 0

def backTracking(x, y, depth):
    global answer
    if depth == k and (x, y) == end:
        answer += 1
    for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != 'T':
            graph[nx][ny] = 'T'
            backTracking(nx, ny, depth + 1)
            graph[nx][ny] = '.'


backTracking(r - 1, 0, 1)
print(answer)
