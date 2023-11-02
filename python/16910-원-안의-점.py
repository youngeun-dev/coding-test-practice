# SWEA 16910 원 안의 점
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYcllbDqUVgDFASR&categoryId=AYcllbDqUVgDFASR&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    answer = 0
    
    for x in range(-N, N + 1):
        for y in range(-N, N + 1):
            if x * x + y * y <= N * N:
                answer +=1
                
    print(f'#{test_case} {answer}')
