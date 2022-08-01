# 주어진 문자열 word가 주어질 때, 해당 단어에서 순서가 바뀐 word를 출력하시오.

word = 'apple'
result = ''
for char in word:
    result = char + result
print(result)
