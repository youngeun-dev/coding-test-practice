def solution(arr, K):
    answer = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if (arr[i] + arr[j] + arr[k]) % K == 0:
                    answer += 1
    return answer
