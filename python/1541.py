num = []

for d in data:
    plus = d.split("+") # data의 원소를 플러스 기준으로 split
    sum = 0 # 더하기 연산을 계산할 변수 
    for i in plus:
        sum += int(i)
    num.append(sum) # 연산 완료 후 num에 저장 

result = num[0] # 첫번째 수
for i in range(1, len(num)):
    result -= num[i] # 차례대로 마이너스 연산 

print(result)
