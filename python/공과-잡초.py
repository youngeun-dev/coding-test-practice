T = int(input())
for test_case in range(1, T + 1):
    
    s = input()
    answer = 0
    answer += s.count('()')
    answer += s.count('(|')
    answer += s.count('|)')
    
    print(f'#{test_case} {answer}')
