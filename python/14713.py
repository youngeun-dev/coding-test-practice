from collections import deque

N = int(input())
arr = list()

for i in range(N):
    arr.append(deque(map(str, input().split())))

sentence = deque(map(str, input().split()))


def is_possible(sentence, arr):
    k = 0
    miss_cnt = 0
    while sentence:
        if arr[k] and sentence[0] == arr[k][0]:
            sentence.popleft()
            arr[k].popleft()
            miss_cnt = 0
        else:
            if miss_cnt == N:
                return False
            miss_cnt += 1
        k = (k + 1) % N

    empty = 0
    for i in range(N):
        if len(arr[i]) == 0:
            empty += 1 

    if not sentence and empty == N:
        return True
    else:
        return False


if is_possible(sentence, arr):
    print("Possible")
else:
    print("Impossible")
