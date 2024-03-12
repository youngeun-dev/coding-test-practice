import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()

for _ in range(m):
    cards[0], cards[1] = cards[0] + cards[1], cards[0] + cards[1]
    cards.sort()

print(sum(cards))

# import sys
# import heapq as hq
# input = sys.stdin.readline

# n, m = map(int, input().split())
# cards = list(map(int, input().split()))
# hq.heapify(cards)

# for _ in range(m):
#     card1 = hq.heappop(cards)
#     card2 = hq.heappop(cards)

#     hq.heappush(cards, card1 + card2)
#     hq.heappush(cards, card1 + card2)

# print(sum(cards))
