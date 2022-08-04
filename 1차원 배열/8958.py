t = int(input())
arr = []

for i in range(t):
    ox_list = list(input())
    score = 0
    score_result = 0
    for j in ox_list:
        if j == 'O':
            score += 1
            score_result += score
        else:
            score = 0
    print(score_result)
