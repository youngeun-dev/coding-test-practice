import sys
input = sys.stdin.readline

day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = [4, 5, 6, 0, 1, 2, 3]

for test_case in range(1, int(input()) + 1):
    m, d = map(int, input().split())

    total_day = 0
    for i in range(m - 1): # 누적 일자 계산
        total_day += day[i]

    total_day += d - 1 

    print(f'#{test_case} {day_of_week[total_day % 7]}')
