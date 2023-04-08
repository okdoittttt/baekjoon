n = int(input())
my_list = []

for i in str(n):
    my_list.append(int(i))

my_list.sort(reverse=True)

for i in my_list:
    print(i, end='')