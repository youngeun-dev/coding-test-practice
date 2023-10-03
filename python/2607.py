# https://www.acmicpc.net/problem/2607
# 비슷한 단어
import sys
input = sys.stdin.readline

n = int(input())
target = input().rstrip()
words = [input().strip() for _ in range(n - 1)]
answer = 0

for word in words:
    if abs(len(word) - len(target)) > 1 or len(set(target).difference(set(word))) > 1:
        continue
    for t in target:
        if t in word:
            word = word.replace(t, "", 1)
    if len(word) <= 1:
        answer += 1

print(answer)
