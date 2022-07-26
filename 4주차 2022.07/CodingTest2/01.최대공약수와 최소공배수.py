# # 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

# 입력 값을 받을 a,b를 선언
a, b = map(int, input().split())

# a,b,c의 결과값을 담을 result 리스트를 생성
a_result_list = []
b_result_list = []
c_result_list = []

# 최대 공약수를 구하기 위한 for문 작성
# 선언했던 a_result에 나머지가 0인 a_least 값을 append
for a_least in range(1, 10001):
    if a % a_least == 0:
        a_result_list.append(a_least)

for b_least in range(1, 10001):
    if b % b_least == 0:
        b_result_list.append(b_least)
# a_result = [1, 2, 3, 4, 6, 8, 12, 24]
# b_result = [1, 2, 3, 6, 9, 18]

# 중첩 for문을 통해 각 list 값이 같은 것들을 c_result에 append
for i in (a_result_list):
    for j in (b_result_list):
        if i == j:
            c_result_list.append(i)

# c_result의 max 값은 최대공배수
# (a*b) 최대공배수로 나눈 값이 최소공약수
print(max(c_result_list))
print(a*b//max(c_result_list))
