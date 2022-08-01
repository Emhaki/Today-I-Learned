# 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
# numbers = input().split()
# print(sum(numbers))

# 오류 해결하기
numbers = map(int, input().split())
print(sum((numbers)))

# input값이 str 형태이기 때문에 int 값으로 형 변환 시키면 오류 해결
