def solution(wallpaper):
    width = len(wallpaper[0])
    height = len(wallpaper)

    h = []
    w = []
    
    for i in range(height):
        for j in range(width):
            if wallpaper[i][j] == "#":
                h.append(i)
                w.append(j)
    
    return [min(h), min(w), max(h) + 1, max(w) + 1]
