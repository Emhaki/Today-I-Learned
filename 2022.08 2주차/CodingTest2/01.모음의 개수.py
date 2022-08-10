# 영문 문장을 입력받아 모음의 개수를 세는 프로그램을 작성하시오. 모음은 'a', 'e', 'i', 'o', 'u'이며 대문자 또는 소문자이다.
import sys
sys.stdin = open('input.txt')

word = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    try:
        word_list = list(map(str, input().split()))
        if word_list[0] == '#':
            break
        else:
            count = 0
            for i in word_list:
                for j in str(i):
                    if j in word:
                        count += 1

            print(count)
    except EOFError:
        break
