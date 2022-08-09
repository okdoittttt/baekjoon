number = set(range(1, 10000))
gen_number = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    gen_number.add(i)

self_num = sorted(number - gen_number)

for i in self_num:
    print(i)
