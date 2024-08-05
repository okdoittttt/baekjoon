from sys import stdin
'''
실버3: 단어 뒤집기 2

rstrip() 함수란?
문자열의 오른쪽에서 공백이나 특정 문자를 제거하거하는 데 사용됨.
예를들어 "hello    " 문자열이 저장된 변수에 사용하면 "hello"가 출력됨.
특정 문자 제거는 매개변수로 넘기므로 가능.
rsplit('h')를 적용하면 "ello"가 출력됨.

만약 리스이 마지막 문자열에 줄바꿈을 하고 싶지 않다면 strip()을 사용해야 한다.
readline()을 사용할 경우 공백 문자까지 모두 리스트에 입력할 수 있다.
*중요* 만약 split()을 사용하면 띄어쓰기 문자를 인식할 수 없다.
'''
# def func(stack):
#     result = []
#     i = 0
#     while i < len(stack):
#         if stack[i] == '<':
#             j = i
#             while j < len(stack) and stack[j] != '>':
#                 j += 1
#
#             result.append(stack[i:j+1])
#             i = j + 1
#         else:
#             start = i
#             while i < len(stack) and stack[i] != '<':
#                 i += 1
#
#             result.append(stack[start:i][::-1])
#
#     return ''.join(result)
#
#
# input_str = input()
# output_str = func(input_str)
# print(output_str)


def reverse_words_outside_brackets(s):
    def reverse_outside(word):
        result = []
        i = 0
        while i < len(word):
            if word[i] == '<':
                j = i
                while j < len(word) and word[j] != '>':
                    j += 1
                result.append(word[i:j+1])
                i = j + 1
            else:
                start = i
                while i < len(word) and word[i] != '<':
                    i += 1
                result.append(word[start:i][::-1])
        return ''.join(result)

    words = s.split(' ')
    reversed_words = [reverse_outside(word) for word in words]
    return ' '.join(reversed_words)


input_str = input()
output_str = reverse_words_outside_brackets(input_str)
print(output_str)
