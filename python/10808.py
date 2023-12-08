import sys
input = sys.stdin.readline

word = input().rstrip()
alpha = [0] * 26

for x in word:
    alpha[ord(x) - 97] += 1

print(*alpha)
