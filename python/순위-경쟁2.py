import sys
input = sys.stdin.readline

n = int(input())
score_a, score_b = 0 , 0
result = 0


def check_score(score_a, score_b):
    if score_a > score_b:
        return 'A'
    elif score_a < score_b:
        return 'B'
    else:
        return 'AB'


for _ in range(n):
    people, score = map(str, input().split())
    
    if people == 'A':
        if check_score(score_a, score_b) != check_score(score_a + int(score), score_b):
            result += 1
        score_a += int(score)

    elif people == 'B':
        if check_score(score_a, score_b) != check_score(score_a, score_b + int(score)):
            result += 1
        score_b += int(score)

print(result)
