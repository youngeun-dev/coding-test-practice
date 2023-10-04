# https://www.acmicpc.net/problem/25757
# 임스와 함께하는 미니게임
import sys
input = sys.stdin.readline

game = {'Y': 1, 'F': 2, 'O': 3}
n, play = map(str, input().split())
people = [input() for _ in range(int(n))]
people = set(people) # 중복 인물 제거

print(len(people) // game[play])
