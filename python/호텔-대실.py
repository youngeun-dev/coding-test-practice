def toTime(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)

def solution(book_time):  
    # 객실의 수 
    room_idx = 0
    
    # 체크인 기준 오름차순 정렬
    book_time.sort(key = lambda x:(x[0]))

    # 객실 체크 아웃 시간 보관
    rooms = [0] * 1001
    
    for book in book_time:
        start, end = toTime(book[0]), toTime(book[1]) + 10
        
        for i in range(room_idx):
            # 기존 객실 사용
            if rooms[i] <= start:
                rooms[i] = end
                break
                
        # 추가 객실이 필요한 경우    
        else:
            rooms[room_idx] = end
            room_idx += 1                
        
    return room_idx
