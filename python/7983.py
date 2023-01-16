import sys
input=sys.stdin.readline

n = int(input()) # N : 과제 개수
homework = [] # 과제 목록
for i in range(n):
    d,t = map(int,input().split()) # d : 과제 소요 시간, t : 과제 마감 기한
    homework.append([d,t])

homework.sort(key=lambda homework:homework[1], reverse=True) # 마감 기한 기준으로 내림차순 정렬

free_day = homework[0][1] # 자유시간 (초기 값)
for i in range(n):
    taken_time = homework[i][0]
    end_time = homework[i][1]

    if end_time <= free_day: # 자유시간 줄이기
        free_day = end_time - taken_time
    else: # 과제 수행 기간이 겹친다면
        free_day = free_day - taken_time


print(free_day)
