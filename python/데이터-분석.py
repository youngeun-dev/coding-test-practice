def solution(datas, ext, val_ext, sort_by):
    # ext 값이 val_ext보다 작은 데이터만 뽑은 후, sort_by에 해당하는 값을 기준으로 오름차순으로 정렬
    ext_dir = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    target_idx = ext_dir[ext]
    sort_target_idx = ext_dir[sort_by]
    
    answer = []
    for data in datas:
        if data[target_idx] <= val_ext:
            answer.append(data)
        
    answer.sort(key=lambda x:(x[sort_target_idx]))
    return answer
