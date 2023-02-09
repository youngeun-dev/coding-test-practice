import sys

# 입력
x, y, c = map(float, sys.stdin.readline().split())

# c를 구하는 함수
def f(w):
    h1 = (x ** 2 - w ** 2) ** 0.5
    h2 = (y ** 2 - w ** 2) ** 0.5
    return (h1 * h2) / (h1 + h2)

# w값 탐색 범위
start, end = 0, min(x,y)

while start <= end:
    mid = (start + end) / 2.0
    find_c = f(mid) # c 계산
    if find_c >= c:
        start = mid
        # 값 c의 오차 범위가 10^−3보다 작아질때까지 이분 탐색
        if abs(find_c - c) < 0.0001: 
            break
    else:
        end = mid

print('%.3f'%start)
