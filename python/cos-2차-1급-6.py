def solution(commands):
    direction = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
    x, y = 0, 0
    for command in commands:
        dx, dy = direction[command]
        x += dx
        y += dy
        
    return [x, y]
