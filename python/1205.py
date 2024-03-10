import sys
input = sys.stdin.readline

n, new_score, p = map(int, input().split())

if n == 0:
    print(1)
else:
    score = list(map(int, input().split()))
    score.append(new_score)
    score.sort(reverse=True)
    index = score.index(new_score)

    if index == p:
        print(-1)
    else:
        if n == p and new_score == score[-1]:
            print(-1)
        else:
            print(index + 1)
