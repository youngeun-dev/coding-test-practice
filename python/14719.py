import sys
input = sys.stdin.readline

# 입력
H, W = map(int, input().split())
data = list(map(int, input().split()))

# 빗물의 총량
answer = 0

# 맨 앞과 맨 뒤는 빗물이 고일 수 없으므로 1 ~ W-1까지 탐색
for i in range(1, W - 1):
    left = max(data[:i]) # 왼쪽에서 가장 높은 블록
    right = max(data[i+1:]) # 오른쪽에서 가장 높은 블록
    min_w = min(left, right)

    # 빗물이 고일 조건 : 양쪽의 블록이 나보다 높으면 됨
    # 좌우의 존재하는 블록의 최댓값의 최솟값이 현재 블록보다 크다면 빗물이 고인다. 
    if min_w > data[i]:
        answer += min_w - data[i]

print(answer)
