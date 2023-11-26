dx = [-1, -2, -2, -1, 1, 2, 1, 2]
dy = [-2, -1, 1, 2, 2, 1, -2, -1]

dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

def check(x, y):
    answer = 0
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
            continue
        else:
            answer += 1
    return answer

def solution(pos):
    x, y = dict[pos[0]], 8 - int(pos[1])
    return check(x, y)
