import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, sys.stdin.readline().split()))
temp = [0] * n

# 줄을 설 사람
for i in range(n):
    # 왼쪽에 있는 키큰 사람
    cnt = 0
    # 줄 설 위치 탐색
    for j in range(n):
        if cnt == data[i] and temp[j] == 0:
            temp[j] = i + 1
            break
        elif temp[j] == 0:
            cnt += 1

print(*temp)
