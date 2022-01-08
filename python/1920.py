n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

def search(m_list):
    start = 0
    end = n - 1

    while(start <= end):
        mid = (start + end) // 2
        if n_list[mid] == m_list:
            return 1

        if n_list[mid] < m_list:
            start = mid + 1
        else:
            end = mid - 1

for i in range(m):
    if search(m_list[i]):
        print(1)
    else:
        print(0)
