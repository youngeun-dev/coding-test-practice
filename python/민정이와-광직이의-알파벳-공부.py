T = int(input())

def DFS(idx, depth, word_sum):
    global answer
    
    if len(set(word_sum)) == 26: 
        answer += 1
        
    if depth == N:
        return 
    
    for i in range(idx, N):
        DFS(i + 1, depth + 1, word_sum + words[i])
    
for test_case in range(1, T + 1):
    N = int(input())
    words = [input() for _ in range(N)]
    answer = 0
    DFS(0, 0, "")
    
    print(f'#{test_case} {answer}')
   
