import sys
input = sys.stdin.readline

n, p, q = map(int, input().split())

dict = { 0 : 1 }
def search(n):
    if n not in dict:
        dict[n] = search(n//p) + search(n//q)
    return dict[n]

print(search(n))
