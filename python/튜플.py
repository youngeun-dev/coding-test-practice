def solution(s):
    dict = {}
    sList = s[2:-2].split('},{')
    
    for sl in sList:
        for num in sl.split(','):
            if int(num) in dict:
                dict[int(num)] += 1
            else:
                dict[int(num)] = 1
                
    result = sorted(dict.items(), key = lambda x: -x[1])
    
    return [x[0] for x in result]
