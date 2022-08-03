import sys
sys.stdin = open('input.txt', "r")

first_place = [1, 3, 6, 10, 15, 21]
first_money = [500, 300, 200, 50, 30, 10]
second_place = [1, 3, 7, 15, 31]
second_money = [512, 256, 128, 64, 32]

T = int(input())
for i in range(T):
    a_money = []
    b_money = []
    a, b = map(int, input().split())
    for g in first_place:
        if a > 21 or a == 0:
            a_money = [0]
        elif a <= g:
            a_money.append(first_money[first_place.index(g)])
    for k in second_place:
        if b > 64 or b == 0:
            b_money = [0]
        elif b <= k:
            b_money.append(second_money[second_place.index(k)])
    result = max(a_money)
    result2 = max(b_money)
    print((result+result2) * 10000)
