def solution(t, p):
    cnt = 0 # 부분문자열 <= p를 만족하는 경우의 수
    for i in range(len(t) - len(p) + 1):
        if (t[i:i+len(p)] <= p):
            cnt += 1
    return cnt
