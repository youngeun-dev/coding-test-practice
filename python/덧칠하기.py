def solution(n, m, section):
    # n: 구역의 개수, m: 롤러의 길이, section: 페인트칠 해야하는 구역의 번호
    answer = 0
    paint = 0 # 어디까지 페인트칠 했는 지 
    for s in section:
        if paint < s: 
            paint = s + m - 1
            answer += 1
            
    return answer
