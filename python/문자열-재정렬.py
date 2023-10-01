# 이코테 문자열 재정렬
import sys
input = sys.stdin.readline

word = list(map(str, input().strip()))
word.sort()

alpha = []
num = []
for w in word:
    if w.isalpha():
        alpha.append(w)
    elif w.isdigit():
        num.append(w)

print(''.join(alpha + num))
