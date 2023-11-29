def solution(phrases, second):
    display = '______________' + phrases
    for i in range(second):
        display = display[1:] + '_'
        print(display)

    return display[:14]
