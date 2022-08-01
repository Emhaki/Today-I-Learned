# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오.
# 양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

number = input()
number = int(number)

# 1. 문자열로 형변환
# print(len(str(number)))

# 2.
result = 0
# number가 0이 아닐때까지
while number != 0:
    number = number // 10
    result += 1

print(result)
