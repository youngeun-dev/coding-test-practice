import sys

input = sys.stdin.readline

N = int(input())
T = [0]
P = [0]
dp = [0] * (N + 1)

# 입력
for _ in range(N):
    x, y = map(int, input().split())
    T.append(x)
    P.append(y)


for i in range(1, N + 1):
    dp[i] = max(dp[i], dp[i - 1]) # i일의 수익 갱신
    end_day = i + T[i] - 1 # 일을 끝낼 수 있는 날
    if end_day <= N: # 퇴사 하기 전이라면
        pay = dp[i - 1] + P[i]
        dp[end_day] = max(dp[end_day], pay)

print(max(dp))
