# https://www.acmicpc.net/problem/21921
# 블로그
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
board = list(map(int, input().split()))

if sum(board) == 0:
    print("SAD")
else:
    answer = temp = sum(board[:k])
    cnt = 1
    for i in range(n - k):
        # 뒤로 한칸씩
        temp += board[i + k]
        temp -= board[i]

        if temp > answer:
            answer = temp
            cnt = 1
        elif temp == answer:
            cnt += 1

    print(answer)
    print(cnt)
