import sys
input = sys.stdin.readline

P = int(input())
for _ in range(P):
    test_case, *students = list(map(int, input().split()))
    cnt = 0
    for i in range(len(students) - 1, 0, -1):
        for j in range(i):
            if students[j] > students[j + 1]:
                cnt += 1
                students[j], students[j + 1] = students[j + 1], students[j]

    print(f'{test_case} {cnt}')
