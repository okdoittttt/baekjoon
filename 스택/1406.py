from sys import stdin
'''
실버2: 에디터
'''
stack = list(input())
N = int(stdin.readline())

point = len(stack)

for i in range(N):
    command = stdin.readline().split()

    if command[0] == 'L':
        if point > 0:
            point -= 1
        else:
            continue
    elif command[0] == 'D':
        if point < len(stack):
            point += 1
        else:
            continue
    elif command[0] == 'B':
        if point > 0:
            stack.remove(stack[point-1])
        else:
            continue
    elif command[0] == 'P':
        stack.insert(point, command[1])
        point += 1


print(''.join(stack))
