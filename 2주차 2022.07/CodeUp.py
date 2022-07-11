# 1. 점심 메뉴가 담긴 리스트를 만들고
# 첫번째 메뉴를 출력

menu = ["짜장면", "김치찌개", "막국수", "닭가슴살"]

print(menu[1])

# 2. 입력받은 숫자에 5를 더한 결과를 출력하세요.
# input은 String 형태로 저장
# int를 통해 변환

num = int(input())
print(num + 5)

# 3. 문자열을 특정 단위로 쪼개기

a = '1 2 3'
print(a.split())
# 쪼갠 문자열 더하기
numbers = a.split()
result = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
print(result)
