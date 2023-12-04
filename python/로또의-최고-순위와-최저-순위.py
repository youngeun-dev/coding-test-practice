rank = [6, 6, 5, 4, 3, 2, 1]
def solution(lottos, win_nums):
    cnt = 0 
    for win_num in win_nums:
        if win_num in lottos:
            cnt += 1
    zero_cnt = lottos.count(0) # 바꿀 수 있는 번호
    return rank[cnt + zero_cnt], rank[cnt]
