T = int(input())

for test_case in range(1, T + 1):
    a, b, c = map(int, input().split())
    bread = a if a < b else b
    answer = c // bread
    print(f'#{test_case} {answer}')
