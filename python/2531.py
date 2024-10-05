import sys
input = sys.stdin.readline

n, d, k, coupon = map(int, input().split())
dishes = [int(input()) for _ in range(n)]
dishes += dishes[:k - 1]

answer = 0
for i in range(n):
    type_of_dish = set(dishes[i:i+k])
    if coupon not in type_of_dish:
        type_of_dish.add(coupon)
    answer = max(answer, len(type_of_dish))

print(answer)
