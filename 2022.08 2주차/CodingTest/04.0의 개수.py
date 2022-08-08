# N부터 M까지의 수들을 종이에 적었을 때 종이에 적힌 0들을 세는 프로그램을 작성하라.

# 예를 들어, N, M이 각각 0, 10일 때 0을 세면 0에 하나, 10에 하나가 있으므로 답은 2이다.
import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    list_ = []
    for i in range(N, M+1):
        for j in str(i):  # 입력받은 숫자들을 str형태로 변환해서 각각 list_에 append
            list_.append(j)
    # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '0']
    if list_.count('0') > 0:  # str형태이기 때문에 count '0'
        print(list_.count('0'))
    else:
        print(0)
