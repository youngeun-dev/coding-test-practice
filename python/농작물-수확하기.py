# SWEA 2805 농작물 수확하기

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]
    start = end = mid = N // 2
    answer = 0
    
    for x in range(N):
        for y in range(start, end + 1):
            answer += graph[x][y]
        if x < mid:
            start -= 1
            end += 1
        elif x >= mid:
            start +=1
            end -= 1
            
    print(f'#{test_case} {answer}')
