# 16진수를 입력받아 8진수(octal)로 출력해보자.

a = input()
n = int(a, 16)  # 입력된 a를 16진수로 인식해 변수 n에 저장
print('%o' % n)
