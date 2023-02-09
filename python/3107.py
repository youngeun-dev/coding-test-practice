import sys

# 입력
IPv6 = list(map(str, sys.stdin.readline().rstrip().split(":")))

# 맨앞/맨뒤에 ::이 존재하는 경우
if IPv6[0] == '':
    IPv6 = IPv6[1:]
if IPv6[-1] == '':
    IPv6 = IPv6[:-1]

# 반복문을 그룹의 총 개수인 8번 수행합니다.
for i in range(8):
    # ''를 가지고 있다면 remove 해주고 부족한 자릿수만큼 0000을 insert 합니다. 
    if IPv6[i] == '':
        IPv6.remove('')
        for _ in range(8 - len(IPv6)):
            IPv6.insert(i, '0000')
    # 빈 문자열도 아니고, 길이가 4가 아니라면 0으로 채워줍니다. 
    else:
        if len(IPv6[i]) != 4:
            IPv6[i] = IPv6[i].zfill(4)


print(':'.join(IPv6))
