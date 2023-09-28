# 이코테 연구소
import sys
input = sys.stdin.readline

# 세로, 가로
N, M = map(int, input().split())

# 연구소 지도
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 벽 설치 후 연구소 지도
after = [[0] * M for _ in range(N)]

# 이동 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 결과
result = 0


# 바이러스 퍼지게 하는 함수
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if after[nx][ny] == 0:
                after[nx][ny] = 2 # 바이러스 전염
                virus(nx, ny)


# 안전 영역 크기 계산
def safe_zone():
    score = 0
    for i in range(N):
        for j in range(M):
            if after[i][j] == 0:
                score += 1
    return score


# DFS를 통해 울타리 설치 -> 안전 영역 크기 계산
def dfs(count):
    global result
    if count == 3:
        for i in range(N):
            for j in range(M):
                after[i][j] = graph[i][j]
        for i in range(N):
            for j in range(M):
                if after[i][j] == 2:
                    virus(i, j)
        result = max(result, safe_zone())
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1


dfs(0)
print(result)
