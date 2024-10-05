import sys
input = sys.stdin.readline

def find_first_key(words):
    for i in range(len(words)):
        if words[i][0].upper() not in cmd:
            cmd.add(words[i][0].upper())
            words[i] = words[i][:0] + "[" + words[i][0] + "]" + words[i][1:]
            return True
    return False


def find_key(words):
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j].upper() not in cmd:
                cmd.add(words[i][j].upper())
                words[i] = words[i][:j] + "[" + words[i][j] + "]" + words[i][j + 1:]
                return

cmd = set()
for _ in range(int(input())):
    words = list(input().split())
    is_finished = find_first_key(words)
    if not is_finished:
        find_key(words)
    print(' '.join(words))



