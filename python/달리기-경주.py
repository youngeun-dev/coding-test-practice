def solution(players, callings):
    player_dict = {p:i for i,p in enumerate(players)}
    index_dict = {i:p for i,p in enumerate(players)}
    
    
    for calling in callings:
        current_index = player_dict[calling] # 현재 인덱스 
        front = index_dict[current_index - 1] # 추월한 선수 이름 
        
        # swap
        player_dict[calling], player_dict[front] = player_dict[front], player_dict[calling]
        index_dict[current_index], index_dict[current_index - 1] = index_dict[current_index - 1], index_dict[current_index]
        
        
    return list(index_dict.values())
