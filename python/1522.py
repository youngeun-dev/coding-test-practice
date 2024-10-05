# https://www.acmicpc.net/problem/1522
# 문자열 교환
import sys
input = sys.stdin.readline

data = list(map(str, input().strip()))
n = data.count('a')
cnt = sys.maxsize

for i in range(len(data)):
    if i + n >= len(data):
        temp = data[i:] + data[:n - (len(data) - i)]
    else:
        temp = data[i: i + n]
    cnt = min(cnt, temp.count('b'))

print(cnt)


# ------------
import sys
input = sys.stdin.readline

words = list(input().rstrip())
a_cnt = words.count('a')
words += words[:a_cnt]
result = 1e9
for i in range(len(words) - a_cnt):
    result = min(result, words[i:i+a_cnt].count('b'))

print(result if result != 1e9 else 0)
