# # 문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.
# count() 메서드 사용 금지

a = input()
a = str(a)
word2 = dict()

for word in a:
    if word in word2:
        word2[word] += 1
    else:
        word2[word] = 1
# print(word2) -> {'a': 1, 'p': 2, 'l': 1, 'e': 1}
# 따라서 word 2의 value값만 출력하면 a의 갯수를 알 수 있다.
print(word2['a'])
