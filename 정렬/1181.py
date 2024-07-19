N = int(input())

word = []

for i in range(N):
    word.append(input())

set_word = set(word)
word = list(set_word)
word.sort()
word.sort(key=len)

for i in word:
    print(i)
