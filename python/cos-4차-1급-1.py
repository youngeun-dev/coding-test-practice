words = []

def create_words(lev, s):
    global words
    VOWELS = ['A', 'E', 'I', 'O', 'U']
    words.append(s)
    for i in range(0, 5):
        if lev < 5:
            create_words(lev + 1, s + VOWELS[i])

def solution(word):
    global words
    words = []
    answer = 0
    create_words(0, '')
    for idx, i in enumerate(words):
        if word == i:
            answer = idx
            break
    return answer
