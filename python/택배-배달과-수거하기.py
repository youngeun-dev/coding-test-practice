# https://school.programmers.co.kr/learn/courses/30/lessons/150369

def solution(cap, n, deliveries, pickups):
    result = 0 # 최소 이동 거리 
    
    have_to_delivery = 0 # 배달해야 할 박스의 개수 
    have_to_pickup = 0 # 수거해야 할 박스의 개수 
    
    for i in range(n): 
        # 먼 곳부터 방문
        have_to_delivery += deliveries.pop() 
        have_to_pickup += pickups.pop() 
        
        print(f'------- {i}번째 집-------')
        print(f'{have_to_delivery}개 배달해야함')
        print(f'{have_to_pickup}개 수거해야함')
        
        while have_to_delivery > 0 and have_to_pickup > 0:
            print(f'{i}번째 집 방문')
            have_to_delivery -= cap
            have_to_pickup -= cap
            result += (n - i) * 2

    return result
