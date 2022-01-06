# 1. 1~10000까지 변수 설정
# 2. 셀프넘버를 담을 변수 설정
# 3. 셀프넘버인 변수에 셀프넘버 담기
# 4. 전체 숫자에서 셀프넘버 빼기
# 5. 출력 !!
# set() 이용하여 중복X

numbers=set(range(1,10001)) # 1~10000 수 담기
self_num=set() # 셀프 넘버 담을 변수 

for i in range(1,10001): # i = 456
    for j in str(i): # j = 4,5,6
        i+=int(j) # i = 456+4+5+6
    self_num.add(i) # 셀프 넘버 추가하기

result=numbers-self_num # 셀프 넘버 아닌수 담기

for k in sorted(list(result)): # list로 변환해서 sort하고 출력
    print(k)
