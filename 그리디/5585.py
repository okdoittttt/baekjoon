'''
타로는 자주 JOI잡화점에서 물건을 산다.
JOI잡화점에는 잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고, 언제나 거스름돈 개수가 가장 적게 잔돈을 준다.
타로가 JOI잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때, 받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.
'''

N = 1000 - int(input())

changes = [500, 100, 50, 10, 5, 1]
coin = 0

for i in changes:
    coin += N//i # 지불해야 할 돈에서 동전을 나눈 몫
    N %= i # 지불해야 할 돈 나머지

print(coin)
