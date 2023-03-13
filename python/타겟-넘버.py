def solution(numbers, target):
    return dfs(numbers, target, 0, 0)

def dfs(numbers, target, sum, index):
    if len(numbers) == index:
        return 1 if sum == target else 0
    else:
        return dfs(numbers, target, sum + numbers[index], index + 1) + dfs(numbers, target, sum - numbers[index], index + 1)
