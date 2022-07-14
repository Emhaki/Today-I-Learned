# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

n = input()
n = str(n)

if n == 'A':
    print('best!!!')
elif n == 'B':
    print('good!!')
elif n == 'C':
    print('run!')
elif n == 'D':
    print('slowly~')
else:
    print('what?')
