def solution(array, commands):
    answer = []
    
    for command in commands:
        # i, j, k 꺼내기
        k = command.pop()
        j = command.pop()
        i = command.pop()
        
        _array = [] # i ~ j번째 숫자를 담을 배열
        for index in range(i, j + 1):
            print(index)
            _array.append(array[index - 1])
        
            
        _array.sort() # 정렬
        answer.append(_array[k - 1]) # K번째 수 append

    return answer
