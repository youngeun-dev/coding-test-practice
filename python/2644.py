# https://www.acmicpc.net/problem/2644
# 촌수계산

import sys
input = sys.stdin.readline


N = int(input())  # 전체 사람의 수
P1, P2 = map(int, input().split())  # 촌수를 구해야 하는 사람
M = int(input())  # 관계의 수

# 부모 - 자식 관계
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부
visited = [False] * (N + 1)

# 계산한 촌수
answer = []


def dfs(now, num):
    num += 1
    visited[now] = True
    if now == P2:
        answer.append(num)

    for nxt in graph[now]:  # 부모-자식 관계 꺼내기
        if not visited[nxt]:  # 방문한 적이 없으면
            dfs(nxt, num)


dfs(P1, 0)
print(-1 if not answer else answer[0] - 1)
