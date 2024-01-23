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
