# 1. 10보다 작으면 앞에 0을 붙여 두 자리 수로 만든 후 각 자리수를 더한다.
# 2. 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 오른쪽 자리 수를 붙여 새로운 수를 만든다.

N = int(input())
num = N
count = 0

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c
    count += 1
    if (num == N):
        break

print(count)