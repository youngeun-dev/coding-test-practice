import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

heap = []
for num in nums:
    hq.heappush(heap, num)

for _ in range(n - 1):
    nums = list(map(int, input().split()))
    for num in nums:
        if num > heap[0]:
            hq.heappop(heap)
            hq.heappush(heap, num)

print(heap[0]) 
