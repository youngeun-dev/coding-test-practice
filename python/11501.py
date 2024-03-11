import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    price = list(map(int, input().split()))

    money = 0  # 이익
    maxPrice = 0  # 주식의 최대 가격
    for i in range(n - 1, -1, -1):
        if maxPrice < price[i]:
            maxPrice = price[i]
        else:
            money += maxPrice - price[i]

    print(money)
