# https://www.acmicpc.net/problem/2565
# 전깃줄

import sys
input = sys.stdin.readline

n = int(input()) # 전깃줄의 개수
data = [] # 전깃줄이 연결되는 위치의 번호가 담긴 배열

for _ in range(n):
    a, b = map(int, input().split())
    data.append([a, b])

dp = [1] * n # 겹치는 횟수를 담을 dp 배열

data.sort(key=lambda x: x[0]) # A 전봇대의 전깃줄 위치를 기준으로 정렬

# LIS : 교차하는 전깃줄이 없는 최댓값 구하기
for i in range(n):
    for j in range(i):
        if data[i][1] > data[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

# 전깃줄의 개수 - 교차하지 않는 전깃줄의 최댓값 == 제거해야하는 전깃줄의 개수
print(n - max(dp))
