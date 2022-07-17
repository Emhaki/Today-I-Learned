# 출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.

n = int(input())
print(min(map(int, input().split())))
