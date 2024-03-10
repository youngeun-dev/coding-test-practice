import sys
input = sys.stdin.readline

AEIOU = ['a', 'e', 'i', 'o', 'u']
CAN_CONTINUE = ['e', 'o']

while True:
    password = input().rstrip()
    if password == 'end':
        break

    pw = list(password)
    v_flag = False  # 모음 존재하는지 확인
    v_cnt = 0  # 모음 3개 연속인지 확인
    c_cnt = 0  # 자음 3개 연속인지 확인
    err = False  # 같은 문자 연속 2개 or 자음/모음 연속 3개인 경우 1
    for i in range(len(pw)):
        # 연속 모음/자음 체크
        if pw[i] in AEIOU:
            v_cnt += 1
            v_flag = True
            c_cnt = 0
        else:
            v_cnt = 0
            c_cnt += 1

        if v_cnt == 3 or c_cnt == 3:
            err = True

        # 같은 문자 연속 체크
        if i > 0:
            if pw[i - 1] == pw[i]:
                if pw[i - 1] in CAN_CONTINUE:
                    continue
                else:
                    err = True

    if not err and v_flag:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')






# while True:
#     password = input().strip()
#     if password == 'end':
#         break
#
#     # 모음 개수
#     v = 0
#     for vowel in AEIOU:
#         if vowel in password:
#             v += 1
#
#     # 부적합: 모음이 존재 X
#     if v == 0:
#         print(f'<{password}> is not acceptable.')
#         continue
#
#     # 부적합: 모음/자음 연속 3번
#     x = 0
#     for i in range(len(password) - 2):
#         if password[i] in AEIOU and password[i + 1] in AEIOU and password[i + 2] in AEIOU:
#             x = 1
#         if password[i] not in AEIOU and password[i + 1] not in AEIOU and password[i + 2] not in AEIOU:
#             x = 1
#
#     if x == 1:
#         print(f'<{password}> is not acceptable.')
#         continue
#
#
#     # 부적합: 같은 글자 연속 2번
#     for i in range(len(password) - 1):
#         if password[i] == password[i + 1]:
#             if password[i] in CAN_CONTINUE:
#                 continue
#             else:
#                 x = 1
#                 break
#     if x == 1:
#         print(f'<{password}> is not acceptable.')
#         continue
#
#     print(f'<{password}> is acceptable.')


