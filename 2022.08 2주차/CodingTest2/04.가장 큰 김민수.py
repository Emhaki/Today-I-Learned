# 은민이는 4와 7을 좋아하고, 나머지 숫자는 싫어한다. 금민수는 어떤 수가 4와 7로만 이루어진 수를 말한다.

# N이 주어졌을 때, N보다 작거나 같은 금민수 중 가장 큰 것을 출력하는 프로그램을 작성하시오.

# N = int(input())

N = input()

find = False

for i in range(2**len(N)):
    answer = ''
    for j in range(len(N)):
        if (i//(2**j)) % 2 == 0:
            answer += ('7'+answer)
        else:
            answer += ('4'+answer)

    if int(answer) <= int(N):
        find = True
        break

if not find:
    answer = ''
    for i in range(len(N)-1):
        answer += '7'

print(answer)
