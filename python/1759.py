import sys
input = sys.stdin.readline


def make_code(idx):
    if len(code) == L:
        c, v = 0, 0 # 자음, 모음
        for x in code:
            if x in aeiou:
                v += 1
            else:
                c += 1
        if c >= 2 and v >= 1:
            print("".join(code))
        return

    for i in range(idx, C):
        code.append(alpha[i])
        make_code(i + 1)
        code.pop()


L, C = map(int, input().split())
alpha = sorted(list(map(str, input().split())))

aeiou = ['a', 'e', 'i', 'o', 'u']
code = []

make_code(0)


# --------
import sys
input = sys.stdin.readline

def check(code):
    aeiou_cnt = 0
    not_aeiou_cnt = 0
    for x in code:
        if x in aeiou:
            aeiou_cnt += 1
        else:
            not_aeiou_cnt += 1

    if aeiou_cnt >= 1 and not_aeiou_cnt >= 2:
        print(''.join(code))


def back_tracking(index):
    if len(code) == L:
        check(code)
        return

    for nxt in range(index, C):
        code.append(alphas[nxt])
        back_tracking(nxt + 1)
        code.pop()


L, C = map(int, input().split())
alphas = list(input().split())
alphas.sort()

aeiou = ['a', 'e', 'i', 'o', 'u']
code = []
back_tracking(0)
