# https://www.acmicpc.net/problem/3758
# KCPC
import sys
input = sys.stdin.readline

# 테스트 케이스 개수
T = int(input())

for _ in range(T):
    # 팀의 개수 n, 문제의 개수 k, 우리 팀 ID team, 로그 엔트리의 개수 m
    n, k, my_team, m = map(int, input().split())
    team_score = [[0] * (k + 1) for _ in range(n + 1)]
    record = [[i, 0, 0, 0] for i in range(n + 1)] # [팀 id, 최종 점수, 제출 횟수, 제출 시간]
    for time in range(m):
        team, idx, score = map(int, input().split())
        if team_score[team][idx] < score:
            team_score[team][idx] = score
            record[team][1] = sum(team_score[team])
        record[team][2] += 1
        record[team][3] = time

    record.sort(key=lambda x: (-x[1], x[2], x[3]))

    for i in range(len(record)):
        if record[i][0] == my_team:
            print(i + 1)
            break
