import sys
input = sys.stdin.readline

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for x in range(N - M + 1):
        for y in range(N - M + 1):
            fly = 0
            for i in range(M):
                for j in range(M):
                    fly += graph[x + i][y + j]

            if answer < fly:
                answer = fly

    print(f'#{test_case} {answer}')
