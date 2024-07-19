'''
실4: 설탕 배달
'''
N = int(input())

sugar = [5, 3]
count = 0

while N >= 0:
    if N % 5 == 0:
        count += int(N//5)
        print(count)
        break

    N -= 3
    count += 1

else:
    print(-1)