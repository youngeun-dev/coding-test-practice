import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 1
cnt = 0

while left <= right and right <= n:
    nums_sum = sum(nums[left:right])
    print(left, right, nums_sum)
    # 수열의 합이 m인 경우 
    if nums_sum == m:
        cnt += 1
        left += 1

    # 수열의 합이 m 초과인 경우 
    elif nums_sum > m:
        left += 1

    # 수열의 함이 m 미만인 경우
    elif nums_sum < m:
        right += 1

print(cnt)
