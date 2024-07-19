n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [float('inf')] * (k + 1)
dp[0] = 0

for i in range(0, k + 1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])


# n, k = map(int, input().split())
#
# coins = []
# for _ in range(n):
#     coins.append(int(input()))
#
# coins.sort(reverse=True)
#
# count = 0
# for coin in coins:
#     count += k // coin
#     k %= coin
#     print(count)
#
# if k == 0:
#     print(count)
# else:
#     print(-1)
