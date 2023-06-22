#https://school.programmers.co.kr/learn/courses/30/lessons/150370

def date_to_day(date):
    year, month, day = map(int, date.split("."))
    return year * 12 * 28 + month * 28 + day 

def solution(today, terms, privacies):
    today = date_to_day(today) # 일 단위로 변환
    
    answer = []
    for i in range(len(privacies)):
        start_date, type = privacies[i].split()  # 공백을 기준으로 문자열을 나누어 리스트로 저장
        start_day = date_to_day(start_date)
        for term in terms:
            find_type, find_term = term.split() 
            if find_type == type and start_day + (int(find_term) * 28) <= today:
                answer.append(i+1)
        
    return answer
