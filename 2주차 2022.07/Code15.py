# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

a = input()
a = str(a)
word2 = []

for i in a:
    if i in word2:
        word2.append(i)
    else:
        word2.append(i)

# word2 = ['b', 'a', 'n', 'a', 'n', 'a']
print(word2.index('a'))

word = input()
word = str(word)
for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx)
        break
else:
    print(-1)
