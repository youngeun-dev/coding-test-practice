import heapq

def solution(scoville, K):
	# answer : 연산 횟수를 담을 변수 
    answer = 0
    # 스코빌 지수 heap으로 변환
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        # 새로운 스코빌 지수 연산
        mix = int(heapq.heappop(scoville)) + int((heapq.heappop(scoville))*2)
        # 새로운 스코빌 지수를 heap에 push
        heapq.heappush(scoville, mix)
        answer += 1
        # 반복문 종료 조건
        if len(scoville) == 1 and scoville[0] < K:
            return -1 
            
    return answer
