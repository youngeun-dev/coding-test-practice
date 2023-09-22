# https://www.acmicpc.net/problem/20920
# 영단어 암기는 괴로워

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N: 단어의 개수, M: 외울 수 있는 단어의 길이

answer = {}

for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        if word in answer:
            answer[word] += 1
        else:
            answer[word] = 1
    else:
        continue

answer = sorted(answer.items(), key = lambda x : (-x[1], -len(x[0]), x[0])) # x[0] = 단어, x[1] = 단어 빈도수
# -x[1] = 자주 나오는 단어
# -len(x[0]) = 길이가 긴 단어
# x[0] = 알파벳 순

for word, count in answer:
    print(word)
