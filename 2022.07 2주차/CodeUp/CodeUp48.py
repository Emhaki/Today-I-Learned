# 월이 입력될 때 계절 이름이 출력되도록 해보자.

n = input()
n = int(n)

if (n == 12 or n == 1 or n == 2):
    print('winter')
elif (n == 3 or n == 4 or n == 5):
    print('spring')
elif (n == 6 or n == 7 or n == 8):
    print('summer')
elif (n == 9 or n == 10 or n == 11):
    print('fall')
