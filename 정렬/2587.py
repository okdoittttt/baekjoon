num_list = []
avg = 0
sum = 0


for i in range(5):
    num_list.append(int(input()))

num_list = sorted(num_list)

middle_index = len(num_list)/2

for i in range(len(num_list)):
    sum += num_list[i]

avg = sum/len(num_list)

print(int(avg))
print(num_list[int(middle_index)])