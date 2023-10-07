# https://www.acmicpc.net/problem/14888
# 연산자 끼워넣기
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
op = list(map(int, input().split()))
max_result = -sys.maxsize
min_result = sys.maxsize

def dfs(depth, plus, minus, multiply, divide, answer):
    global max_result, min_result
    if depth == n:
        max_result = max(answer, max_result)
        min_result = min(answer, min_result)
        return
    if plus:
        dfs(depth + 1, plus - 1, minus, multiply, divide, answer + data[depth])
    if minus:
        dfs(depth + 1, plus, minus - 1, multiply, divide, answer - data[depth])
    if multiply:
        dfs(depth + 1, plus, minus, multiply - 1, divide, answer * data[depth])
    if divide:
        dfs(depth + 1, plus, minus, multiply, divide - 1, int(answer / data[depth]))


dfs(1, op[0], op[1], op[2], op[3], data[0])
print(max_result)
print(min_result)
