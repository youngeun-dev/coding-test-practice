from itertools import product

def solution(users, emoticons):
    # 사용자 수, 이모티콘 수 
    n, m = len(users), len(emoticons)
    
    # 이모티콘 플러스 가입자
    total_joiner = 0
    # 이모티콘 매출액
    total_cost = 0
    
    # 중복 순열로 할인율 조합 찾기 
    discounts = product([10,20,30,40], repeat = m)
    
    for discount in discounts:
        # 각 조합별 이모티콘 판매액, 플러스 가입자 수 
        sum_cost = 0
        joiner = 0
        
        for user in users:
            # 사용자의 구매 기준
            rate, max_cost = user
            # 사용자의 이모티콘 결제 금액
            buy_cost = 0
            
            for i, emoticon in enumerate(emoticons):
                if discount[i] >= rate:
                    # 할인된 가격
                    buy_cost += emoticon * (100 - discount[i]) * 0.01
            
            if buy_cost >= max_cost:
                joiner += 1
            else:
                sum_cost += buy_cost
        
        # 이모티콘 플러스 가입자가 더 많은 경우 
        if total_joiner < joiner:
            total_joiner = joiner
            total_cost = sum_cost
        # 가입자 수는 같은데, 판매액이 더 많은 경우 
        elif total_joiner == joiner:
            if total_cost < sum_cost:
                total_cost = sum_cost 

    return [total_joiner, total_cost]
