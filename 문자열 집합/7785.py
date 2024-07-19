N = int(input())

leave = set()
result = set()

for i in range(N):
    name, state = input().split()

    if state == 'enter':
        result.add(name)
    elif state == 'leave':
        leave.add(name)

result = result.difference(leave)

for i in sorted(result, reverse=True):
    print(i)

