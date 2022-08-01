# 1545. 거꾸로 출력해 보아요 D1

# 주어진 숫자부터 0까지 순서대로 찍어보세요

n = int(input())

while n != -1:
    print(n, end=" ")
    n -= 1
