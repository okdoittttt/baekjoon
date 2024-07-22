import sys
'''
실버5: 괄호
'''

N = int(input())

for i in range(N):
    stack = []
    W = input()

    for j in W:
        if j == '(':
            stack.append(j)
        elif j == ')':
            # )를 정상적으로 pop 하는 경우
            if len(stack) != 0:
                stack.pop()
            # 스택이 비어있는 경우
            else:
                print('NO')
                break

    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')

