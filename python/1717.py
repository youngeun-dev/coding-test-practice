# n = 집합의 개수 / m = 연산의 개수
n,m=map(int,input().split())

parent = [0] * (n+1) # 부모 테이블 생성
for i in range(n+1): # 자기 자신을 부모로 설정
    parent[i]=i

def find(x): # 루트 노드를 찾는 함수
    if parent[x] == x: # 자기 자신이 부모이면 반환
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    if x < y:
        parent[find(y)] = find(x)
    else:
        parent[find(x)]=find(y)

for _ in range(m):
    cmd, a, b=map(int,input().split())
    if cmd == 0:
        union(a,b)
    elif cmd==1:
        if find(a)==find(b):
            print("YES")
        else:
            print("NO")
