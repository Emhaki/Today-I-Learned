# 친구들과 함께 3 6 9 게임을 하던 영일이는 잦은 실수 때문에 계속해서 벌칙을 받게 되었다.
# 3 6 9 게임의 왕이 되기 위한 369 마스터 프로그램을 작성해 보자.

n = int(input())

for i in range(1, n+1):
    if i % 10 == 3:
        print("X", end=' ')
    elif i % 10 == 6:
        print("X", end=' ')
    elif i % 10 == 9:
        print("X", end=' ')
    else:
        print(i, end=' ')
