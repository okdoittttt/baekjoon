import sys
'''
실버2: 스택 수열
'''
N = int(sys.stdin.readline())

stack = []
result = []
cur = 1

for i in range(N):
    num = int(sys.stdin.readline())

    # 입력된 숫자까지 스택에 push
    while cur <= num:
        stack.append(cur)
        result.append('+')
        cur += 1

    if stack[-1] == num:
        stack.pop()
        result.append('-')

    else:
        print('NO')
        break


if len(stack) == 0:
    for j in result:
        print(j)


# 스택을 2개 사용하는 방법
# 시간 초과 해결
from sys import stdin

left = list(input())
right = []

for _ in range(int(input())):
    command = list(stdin.readline().split())
    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

answer = left + right[::-1]
print(''.join(answer))