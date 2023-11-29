def solution(bishops):
    visited = [] # 말을 놓을 수 없는 좌표 
    answer = 64 # 말을 놓을 수 있는 최대 수 
    direction = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for a, b in bishops:
        for i in range(4):
            x, y = 8 - int(b), ord(a) - 65
            if [x, y] not in visited:
                visited.append([x, y])
            while 0 <= x < 8 and 0 <= y < 8:
                x = x + direction[i][0]
                y = y + direction[i][1]
                if 0 <= x < 8 and 0 <= y < 8 and [x, y] not in visited:
                    visited.append([x, y])

    return answer - len(visited)
