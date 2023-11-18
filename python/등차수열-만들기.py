for test_case in range(1, int(input()) + 1):
    a, b, c = map(int, input().split())

    if b - a == c - b:  # 이미 등차수열을 이루고 있는 경우
        answer = 0.0
    else:
        answer = abs((b - a) - (c - b)) / 2

    print(f'#{test_case} {answer}')
