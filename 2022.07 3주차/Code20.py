# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요.

# input
# 123

# output
# 6

n = map(int, input())

s = []

for i in n:
    s.append(i)
# s에 입력값을 하나씩 list 형태로 저장
# [1,2,3]
# sum(s)를 통해 각 인덱스 값의 합을 출력
print(sum(s))

# for j in range(1, len(s)+1):
#     result = sum(s)
# # for range 1~ s의 길이+`로 범위를 설정하고
# # s 리스트의 합을 result 값에 할당
# print(result)

# 이러한 방법도 존재
# number, remainder = divmod(number, 10)
# result += remainder

# print(result)
