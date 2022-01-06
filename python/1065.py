def hansu(num): # 한 수 함수 정의
    hansu_cnt=0 # 한수 개수를 담는 변수 
    for i in range(1,num+1): # 1~입력받은 수 까지
        num_list = list(map(int,str(i))) # list 만들어줌 
        if i<100:
            hansu_cnt+=1 # 100이하는 다 등차수열 == 한수
        elif num_list[1]-num_list[0] == num_list[2]-num_list[1]: # 각각 자리수의 차가 같다면 한수이다
                    hansu_cnt+=1
    return hansu_cnt

num = int(input()) # 수 입력
print(hansu(num)) # 한 수 출력
