# 문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

a = input()
a = str(a)
word2 = dict()

for word in a:
    if word in word2:
        word2[word] += 1
    else:
        word2[word] = 1

for i in word2:
    print(i, word2[i])
