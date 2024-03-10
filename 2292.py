import sys
input = sys.stdin.readline

n = int(input())
cnt ,room = 1, 1
while room < n:
    room += 6 * cnt
    cnt += 1
    
print(cnt)
