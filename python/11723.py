# https://www.acmicpc.net/problem/11723
# 집합

import sys
input = sys.stdin.readline


def add(n):
    S.add(n)


def remove(n):
    S.discard(n)


def check(n):
    print(1 if n in S else 0)


def toggle(n):
    if n in S:
        remove(n)
    else:
        add(n)


def empty():
    S.clear()


def all_numbers():
    empty()
    for i in range(1, 21):
        add(i)


M = int(input())  # 연산 횟수
S = set()

for _ in range(M):
    command = input().strip().split()
    if command[0] == "all":
        all_numbers()
    elif command[0] == "empty":
        empty()
    elif command[0] == "add":
        add(int(command[1]))
    elif command[0] == "remove":
        remove(int(command[1]))
    elif command[0] == "check":
        check(int(command[1]))
    elif command[0] == "toggle":
        toggle(int(command[1]))
