T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    num = b - a
    if num == 0:
        answer = 0
    elif num <= 1:
        answer = -1
    elif num % 2 == 0:
        answer = num // 2
    elif num >= 3:
        answer = (num - 3) // 2 + 1
    print(f'#{test_case} {answer}')
