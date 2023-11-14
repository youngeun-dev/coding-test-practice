import sys
input = sys.stdin.readline

for test_case in range(1, int(input()) + 1):
    answer = 0
    temp = ord('a')

    for x in input():
        if ord(x) == temp:
            answer += 1
            temp += 1
        else:
            break

    print(f'#{test_case} {answer}')
