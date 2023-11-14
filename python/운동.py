import sys
input = sys.stdin.readline


def DFS(now, dist, start):
    global answer
    visited[now] = 1
    for nxt, nxt_dist in graph[now]:
        cost = dist + nxt_dist
        if not visited[nxt]:
            if cost < answer:
                DFS(nxt, cost, start)
        elif nxt == start:
            answer = min(answer, cost)


for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())  # N: 건물 개수, M: 도로 개수
    graph = [[] for _ in range(N + 1)]  # 도로의 정보
    for _ in range(M):
        s, e, c = map(int, input().split())
        graph[s].append((e, c))

    answer = 1e9
    for i in range(1, N + 1):
        visited = [0] * (N + 1)
        DFS(i, 0, i)

    print(f'#{test_case} {answer}')
