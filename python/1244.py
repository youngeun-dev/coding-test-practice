import sys
input = sys.stdin.readline


def change_switch(idx):
    switch[idx] = 0 if switch[idx] else 1


n = int(input())
switch = [0] + list(map(int, input().split()))
student = int(input())

for _ in range(student):
    sex, num = map(int, input().split())
    if sex == 1: # 남학생
        for i in range(num, n + 1, num):
            change_switch(i)
    elif sex == 2: # 여학생
        change_switch(num)
        for i in range(1, n // 2):
            if num - i < 1 or num + i > n:
                break
            if switch[num - i] != switch[num + i]:
                break
            else:
                change_switch(num - i)
                change_switch(num + i)


for i in range(1, n + 1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()
