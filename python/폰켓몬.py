def solution(nums):
    answer = 0 
    max_length = len(nums) // 2 # 2/N 길이 
    type_size = len(set(nums)) # type의 개수 
    
    if max_length < type_size:
        answer = max_length
    else:
        answer = type_size
    
    return answer
