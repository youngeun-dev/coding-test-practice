def solution(name):
    move_char = 0
    move_location = len(name) - 1
    
    for i, char in enumerate(name):
        # 알파벳 이동 횟수 
        move_char += min(ord('Z') - ord(char) + 1, ord(char) - ord('A'))
        
        # 해당 알파벳 다음에 존재하는 연속된 A 찾기
        nxt = i + 1
        while nxt < len(name) and name[nxt] == 'A':
            nxt += 1
            
        # 이동 횟수 
        move_location = min(move_location, 2 * i + len(name) - nxt, i + 2 * (len(name) - nxt))
        
            
    return move_char + move_location
