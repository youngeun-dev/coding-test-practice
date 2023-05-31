def solution(keymap, targets):
    answer = []
    for target in targets: 
        times = 0 
        for alpha in target: 
            time = 101
            flag = False
            for key in keymap: 
                if alpha in key: 
                    time = min(key.index(alpha)+1, time)
                    flag = True
            
            if flag == False: 
                times = -1 
                break
            times += time
                    
        answer.append(times)
                
    return answer
