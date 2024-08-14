from sys import stdin
'''
실버2: 잃어버린 괄호
값을 최소로 만들기
1. 가장 큰 수에 '-' 부여, 가장 작은 수에 '+' 부여
2. 즉 + 부분을 가장 먼저 계산한 후(괄호) 나머지를 빼면 된다.
'''
A = list(map(str, input().split("-")))
result = 0
# print(A)


def mySum(i):
    sum = 0
    temp = str(i).split('+')

    for i in temp:
        sum += int(i)

    return sum


for i in range(len(A)):
    temp = mySum(A[i])
    if i == 0:
        result += temp
    else:
        result -= temp

print(result)
