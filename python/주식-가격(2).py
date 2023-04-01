from collections import deque

def solution(prices):
    answer = []
    # deque로 변환
    prices = deque(prices)
    
    while prices:
        time = 0
        # 맨 앞 원소를 pop
        left_price = prices.popleft()
        # 그 다음 원소부터 비교
        for right_price in prices:
            if left_price > right_price:
                time += 1
                break
            else:
                time += 1
        answer.append(time)
    
    return answer
