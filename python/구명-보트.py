def solution(people, limit):
    people.sort()
    start, end = 0, len(people) - 1
    boat = 0
    
    while start <= end:
        
        # 무게가 가장 적은 사람과 많은 사람 탑승
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
            
        # 무게 많은 사람 혼자 탑승 
        else:
            end -= 1
    
        # 구명 보트 수 증가
        boat += 1
        
    return boat
