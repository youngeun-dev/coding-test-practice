import sys
input = sys.stdin.readline

# -- 입력 --
# N : 의뢰 개수, K : 연속으로 거절할 수 있는 최대 횟수
# data : 의뢰 요청 리스트
N, K = map(int, input().split()) 
data = list(map(int, input().split())) 


start = 0 # start : 탐색을 시작할 인덱스 번호
answer = 0

# 의뢰 개수만큼 반복합니다. 
for _ in range(N): 
    end = 0
    min_cost = 10**9
    
    # K개의 의뢰 중에서 최소 하나 이상의 의뢰는 받아야 하므로 
    # start ~ start + K 만큼 반복문을 수행해 의뢰 비용이 적은 의뢰를 찾습니다. 
    for j in range(start, start + K):
    	# min_cost = min(data[j], min_cost)
        if data[j] < min_cost:
            min_cost = data[j]
            end = j # end : min_cost를 업데이트한 인덱스로 업데이트 

	# K개씩 탐색해 업데이트된 min_cost와 answer의 최댓값으로 answer를 업데이트합니다.
	# answer = max(answer, min_cost)
    if answer < min_cost: 
        answer = min_cost

    # end는 최솟값을 업데이트한 인덱스이므로 end + 1부터 end + 1 + K까지 탐색합니다. 
    # end + 1 + K 이 의뢰 개수를 초과한다면 data의 크기를 벗어나기 때문에 탐색이 종료됩니다. 
    # 탐색이 가능하다면 start를 end + 1로 업데이트한 후 또 다시 탐색합니다. 
    if end + 1 + K > N: break 
    else: start = end + 1 

print(answer)
