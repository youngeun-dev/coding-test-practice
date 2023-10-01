# 이코테 럭키 스트레이트
import sys
input = sys.stdin.readline

score = list(map(int, input().strip()))
mid_idx = int(len(score) // 2)

left = sum(score[:mid_idx])
right = sum(score[mid_idx:])

print("LUCKY" if left == right else "READY")
