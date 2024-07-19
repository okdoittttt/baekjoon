import sys


N, M = map(int, sys.stdin.readline().split())

pokemon = {}
search = []
result = []

for i in range(1, N+1):
    number = i
    name = sys.stdin.readline()
    pokemon[number] = name

for i in range(M):
    keywords = sys.stdin.readline()
    search.append(keywords)

for item in search:
    try:
        item = int(item)
    except:
        item = item

    if type(item) == int:
        for key, val in pokemon.items():
            if key == item:
                result.append(val)
    else:
        for key, val in pokemon.items():
            if val == item:
                result.append(key)


for i in range(M):
    print(result[i])

