# 입력
N, H = map(int, input().split())  # 동굴 길이, 높이

down = []  # 석순의 높이
up = []  # 종유석의 높이
for i in range(N):
    if i % 2 == 0:
        down.append(int(input()))
    else:
        up.append(int(input()))
        
        
count = 0  # 최소 충돌 구간 개수
min_crash = N  # 최소 장애물 충돌 개수

# 정렬
down.sort()
up.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return len(array) - start


for fly in range(1, H + 1):
    up_crash = binary_search(up, fly - 0.5, 0, len(up)-1)
    down_crash = binary_search(down, H - fly + 0.5, 0, len(down)-1)
    crash = up_crash + down_crash
    if min_crash == crash:
        count += 1
    elif min_crash > crash:
        count = 1
        min_crash = crash

print(min_height, count)
