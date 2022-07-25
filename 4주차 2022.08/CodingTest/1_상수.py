# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b = input().split()

a_list = []  # 734
b_list = []  # 893

# 입력값을 리스트에 삽입
for i in a:
    a_list.append(i)
for j in b:
    b_list.append(j)
# a_list = ['7','3','4']
# b_list = ['8','9','3']

# 임시값을 할당해서 각 리스트 0과 2 인덱스 값을 교환
temp = a_list[0]
a_list[0] = a_list[2]
a_list[2] = temp

temp2 = b_list[0]
b_list[0] = b_list[2]
b_list[2] = temp2

# a_list = ['4', '3', '7']
# b_list = ['3', '9', '8']
result = a_list[0]+a_list[1]+a_list[2]
result2 = b_list[0]+b_list[1]+b_list[2]
# 437
# 398
if result > result2:
    print(result)
else:
    print(result2)
