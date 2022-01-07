# 이것이 취업을 위한 코딩테스트다 떡볶이 떡

# n 은 떡의 개수
# m 은 요청한 떡의 길이

n, m = map(int, input().split())
array = list(map(int, input().split()))
# array.sort()

start = 0
end = max(array)

# 절단 위치
result = 0

while(start <= end):

    total = 0 # 총 잘리는 떡의 길이
    mid = (start+end)//2

    for x in array:
        if x > mid:  # 절단기 길이보다 떡 길이가 길면 절단 가능
            total += x - mid    # 떡길이 - 절단기 길이

    if total < m:           # 요청한 떡 길이보다 작으면? > 더 잘라야됨 > 종료점을 땡겨야함
        end = mid - 1

    else:  # 필요한 떡의 길이가 요청한 길이보다 클 경우 > 최대한 덜 잘라야 함 > 시작점 증가

        result = mid
        start = mid + 1   # (종료점을 증가시킬 순 없고, 종료점을 땡기면 떡의 길이가 더 길어짐)

print(result)
