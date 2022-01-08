# 입력 시간 줄이기
import sys
num = sys.stdin.readline

arr = list()
ouput_arr = list()

# 입력
for i in range(int(num())):
    arr.append(int(input()))

# sorted는 sort처럼 정렬된 리스트를 저장하지 않음, 대신 더 빠름
# arr 리스트는 입력 받은 그대로 임
ouput_arr = sorted(arr)

# 정렬 원소 출력
for i in ouput_arr:
    print(i)
