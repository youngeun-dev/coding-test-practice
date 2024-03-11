import sys
from collections import Counter

input = sys.stdin.readline

P = int(input())

for test_case in range(P):
    n = int(input())
    team_rank = list(map(int, input().split()))

    # 팀 개수
    team_num = max(team_rank)

    # 6명 이하인 팀 거르
    counter = Counter(team_rank)
    not_team = []
    for i in range(1, team_num + 1):
        if counter[i] < 6:
            not_team.append(i)

    # 점수 계산
    score = 1
    graph = {}
    for i in range(n):
        if team_rank[i] not in not_team:
            if team_rank[i] in graph:
                # 다섯번째 팀원 점수 추가
                if graph[team_rank[i]][0] == 4:
                    graph[team_rank[i]][0] += 1
                    graph[team_rank[i]][2] = score
                # 4명이 될 때까지 점수 업데이트 
                elif graph[team_rank[i]][0] < 4:
                    graph[team_rank[i]][0] += 1
                    graph[team_rank[i]][1] += score

            else:
                # 첫 멤버 
                graph[team_rank[i]] = [1, score, 0]
            score += 1

    # 우승팀 
    winner = sorted(graph.items(), key=lambda x: (x[1][1], x[1][2]))[0][0]
    print(winner)


        




