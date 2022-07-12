# 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

# for 문
n = int(input())
for j in range(n):
    num = 1
    for i in range(j + 1):
        num = num * (i + 1)
print(num)

# while 문
n = int(input())
num = 1
i = 1
while i <= n:
    num *= i
    i += 1
print(num)
