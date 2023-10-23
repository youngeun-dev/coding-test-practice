# https://www.acmicpc.net/problem/1459
# 걷기
import sys
input = sys.stdin.readline

x, y, w, s = map(int, input().split())
max_walk, min_walk = max(x, y), min(x, y)

# 평행 이동
dist1 = (x + y) * w

# 대각 이동
dist2 = max_walk * s if (x + y) % 2 == 0 else (max_walk - 1) * s + w

# 평행 + 대각 이동
dist3 = (min_walk * s) + ((max_walk - min_walk) * w)

print(min(dist1, dist2, dist3))
