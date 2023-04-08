# https://www.acmicpc.net/problem/1059
# 좋은 구간

import sys

input = sys.stdin.readline

# 입력
L = int(input().strip())  # S의 길이
S = list(map(int, input().split()))
N = int(input().strip())

# 정렬
S.sort()

# N이 집합에 존재하는 경우 - 0 출력
if N in S:
    print(0)
else:
    start = 0
    end = 0
    for num in S:
        if num < N:
            start = num
        elif num > N and end == 0: # end가 계속 갱신 되지 않도록!
            end = num
    # 해당 숫자는 제외해주기
    start += 1
    end -= 1
    print((N-start)*(end-N+1) + (end-N))
