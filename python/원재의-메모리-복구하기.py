# SWEA 원재의 메모리 복구하기 

T = int(input())

for test_case in range(1, T + 1):
    target = input()
    origin = ['0'] * len(target)
    answer = 0
    
    for i in range(len(target)):
        if target[i] != origin[i]:
            for j in range(i, len(target)) :
                origin[j] = target[i]
            answer += 1
            
    print(f'#{test_case} {answer}')
