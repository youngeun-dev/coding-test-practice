def solution(sizes):
    
    weight = []
    length = []
    
    for x, y in sizes:
        if x >= y:
            weight.append(x)
            length.append(y)
        else:
            weight.append(y)
            length.append(x)
        
    return max(weight) * max(length)
