import sys
input = sys.stdin.readline


def format_time(time):
    hour, minute = time.split(":")
    return (int(hour) * 60) + int(minute)


S, E, Q = input().split()
S, E, Q = format_time(S), format_time(E), format_time(Q)

dict = {}
answer = 0
while True:
    try:
        time, name = input().split()
        if format_time(time) <= S:
            dict[name] = 1
        elif E <= format_time(time) <= Q and name in dict:
            del dict[name]
            answer += 1
    except:
        break

print(answer)
