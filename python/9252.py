string1 = [''] + list(input().strip())
string2 = [''] + list(input().strip())

len1 = len(string1)
len2 = len(string2)

board = [['' for _ in range(len1)] for _ in range(len2)]

for i in range(1, len2):
    for j in range(1, len1):
        if string1[j] == string2[i]:
            board[i][j] = board[i - 1][j - 1] + string1[j]
        else:
            if len(board[i - 1][j]) > len(board[i][j - 1]):
                board[i][j] = board[i - 1][j]
            else:
                board[i][j] = board[i][j - 1]

answer = len(board[-1][-1])
print(answer)
if answer != 0:
  print(board[-1][-1])
