import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

left, right = 0, 0
counter = [0] * (max(data) + 1)

answer = 0
while right < n:
    if counter[data[right]] < k:
        counter[data[right]] += 1
        right += 1
    else:
        counter[data[left]] -= 1
        left += 1
    answer = max(answer, right - left)

print(answer)
