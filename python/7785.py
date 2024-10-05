IN = "enter"
OUT = "leave"

result = {}
for _ in range(int(input())):
    name, method = input().split()
    if method == IN:
        result[name] = method
    elif method == OUT:
        del result[name]

result = sorted(result.keys(), reverse=True)
for name in result:
    print(name)
