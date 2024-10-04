n = int(input())
nums = list(map(int, input().split()))

dp = [1] * n

for end in range(1, n):
    for front in range(end):
        if nums[front] < nums[end]:
            dp[end] = max(dp[end], dp[front] + 1)

size = max(dp)
print(size)

answer = []
for i in range(n - 1, -1, -1):
    if dp[i] == size:
        answer.append(nums[i])
        size -= 1

print(*answer[::-1])
