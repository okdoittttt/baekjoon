N, M = map(int, input().split())

set_A = set()
set_B = []

count = 0

for i in range(N):
    data = input().rstrip()
    set_A.add(data)  # set은 add로 데이터 추가

for i in range(M):
    data = input().rstrip()
    if data in set_A:
        count+=1


# print(set_A)
# print(set_B)
print(count)
