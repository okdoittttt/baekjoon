import sys

arr = sys.stdin.readline

board = []

for i in range(9):
    board.append(list(map(int, input().split())))

X = 0
Y = 0
max_num = -1

for i in range(9):
    for j in range(9):
        if board[i][j] > max_num:
            max_num = board[i][j]
            X = i+1
            Y = j+1

print(max_num)
print(X, Y)