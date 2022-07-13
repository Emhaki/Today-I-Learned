# 주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.

x = str(input())


def find_word(x):
    return x != 'a'


result = list(filter(find_word, x))
print(result.pop(0)+result.pop(0)+result.pop(0)+result.pop(0))
