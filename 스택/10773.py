import sys
'''
실버4: 제로
'''

K = int(sys.stdin.readline())

stack = []

for i in range(K):
    num = int(sys.stdin.readline())

    if num != 0:
        stack.append(num)
    elif num == 0:
        stack.pop()

print(sum(stack))