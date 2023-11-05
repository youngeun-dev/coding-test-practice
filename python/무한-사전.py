T = int(input())

for test_case in range(1, T + 1):
    p = input().rstrip()
    q = input().rstrip()
    if p + 'a' == q:
        print(f'#{test_case} N')
    else:
        print(f'#{test_case} Y')
