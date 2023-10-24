# https://www.acmicpc.net/problem/1941
# 소문난 칠공주
import sys
from collections import deque
input = sys.stdin.readline


def BFS(princess): # 7명이 모여있는지 체크
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited = [[1] * 5 for _ in range(5)]

    for i in princess:
        visited[i[0]][i[1]] = 0 # 7명 위치 갱신

    q = deque([princess[0]])
    visited[princess[0][0]][princess[0][1]] = 1 # 첫번째 위치 방문
    check = 1 # 방문 횟수
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                check += 1
                q.append((nx, ny))
                if check == 7:
                    return True

    return False


def DFS(start, count):
    global answer

    if count >= 4: # 임도연파가 4명 이상이면 안됨
        return

    if len(princess) == 7: # 학생이 7명 모여졌으면
        if BFS(princess):
            answer += 1
        return

    for i in range(start, 25): # 조합
        r = i // 5
        c = i % 5
        princess.append((r, c))
        DFS(i + 1, count + (board[r][c] == 'Y'))
        princess.pop()


board = [list(input().strip()) for _ in range(5)]
answer = 0 # 소문난 칠공주 수
princess = [] # 학생들의 좌표를 담을 배열

DFS(0, 0)
print(answer)
