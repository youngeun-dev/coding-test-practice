import sys
input = sys.stdin.readline

for test_case in range(1, int(input()) + 1):
    # input
    n = int(input())
    price = list(map(int, input().split()))

    # output
    answer = 0

    # 초기 판매 가격
    max_value = price[-1] 
    for i in range(n - 2, -1, -1):
        # 더 큰 값으로 판매 가격 조정
        if max_value < price[i]:
            max_value = price[i]
        # 사고 팔기 
        elif max_value > price[i]:
            answer += (max_value - price[i])

    print(f'#{test_case} {answer}')
