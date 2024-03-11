import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 0
answer = 1e9
sum = 0

while left <= right:
    if sum >= s:
        answer = min(answer, right - left)
        sum -= nums[left]
        left += 1
    elif right == n:
        break
    else:
        sum += nums[right]
        right += 1

print(answer) if answer < 1e9 else print(0)
