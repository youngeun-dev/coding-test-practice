import sys

# 입력
n = int(sys.stdin.readline())  # 회의의 수 N

for _ in range(n): # 회의 시간 입력
    start, end = map(int, input().split())
    time.append([start, end])

time = []  # 회의 시간
count = 1  # 회의의 개수

time.sort(key=lambda x: (x[1], x[0])) # 시작시간, 종료시간을 기준으로 회의 시간 정렬

end_time = time[0][1] # 첫 회의 종료 시간
for i in range(1, n):
    if end_time <= time[i][0]: # 회의 종료 시간과 같거나 큰 회의 시작 시간이 있다면
        end_time = time[i][1] # 회의 종료 시간 갱신
        count += 1 # 최대 회의 개수 증가

print(count)
