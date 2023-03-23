from collections import deque

def solution(begin, target, words):
    q = deque()
    q.append([begin, 0])
    
    visit = [0] * len(words)
    
    # words에 target이 존재하지 않는다면 변환을 할 수 없음
    if target not in words:
        return 0
    
    while q:
        word, cnt = q.popleft()
        
        if target == word:
            return cnt
        
        for i in range(len(words)):
            different_cnt = 0
            
            if not visit[i]: # 방문 여부 확인 
                
                # 알파벳 몇개가 다른 지 찾기
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        different_cnt += 1
                        
                # 알파벳 1개가 다르다면 단어 바꾸기        
                if different_cnt == 1:
                    visit[i] = 1
                    q.append([words[i], cnt+1])
                    
    return 0
