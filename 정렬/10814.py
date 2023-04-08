N = int(input())

my_list = []

for i in range(N):
    age, name = map(str, input().split())
    age = int(age)
    my_list.append((age, name))

my_list.sort(key=lambda x : x[0])

for i in my_list:
    print(i[0], i[1])

