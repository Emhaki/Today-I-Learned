# 1. 문자(character)는
# 0~9, a~z, A~Z, !, @, #, {, [, <, ... 과 같이
# 길이가 1인 기호라고 할 수 있다.

# 변수에 문자 1개를 저장한 후
# 변수에 저장되어 있는 문자를 그대로 출력해보자.

c = input()
print(c)

# 2. 공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.

a, b = input().split()
a = int(a)
b = int(b)
print(a)
print(b)

# 3. 24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.
a, b = input().split(':')
print(a, b, sep=':')

# 4. "연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.
y, m, d = input().split('.')
print(d + "-" + m + "-" + y)
