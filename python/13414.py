max_capacity, student_cnt = map(int, input().split())

answer = {}
for i in range(1, student_cnt + 1):
    answer[input()] = i

answer = sorted(answer.items(), key=lambda x:x[1])

if max_capacity > len(answer):
    max_capacity = len(answer)

for i in range(max_capacity):
    print(answer[i][0])
