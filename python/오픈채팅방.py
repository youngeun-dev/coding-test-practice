def solution(record):
    answer = []
    change = {}
    
    for r in record:
        info = r.split()
        if info[0] in ("Change", "Enter"):
            change[info[1]] = info[2]
            
    for r in record:
        info = r.split()
        command, user_id = info[0], info[1]
                    
        if info[0] == "Enter":
            answer.append(f'{change[user_id]}님이 들어왔습니다.')
        elif command == "Leave":
            answer.append(f'{change[user_id]}님이 나갔습니다.')
            
    return answer
