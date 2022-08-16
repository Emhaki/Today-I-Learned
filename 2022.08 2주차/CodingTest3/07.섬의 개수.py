# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.

# 둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

# 입력의 마지막 줄에는 0이 두 개 주어진다.

from pprint import pprint
import sys

sys.stdin = open('input.txt')
w, h = map(int, input().split())  # w는 행 h는 열

matrix = []
for _ in range(w):  # 행
    matrix.append(input().split())  # 열

# [['1', '0', '1', '0', '1'],
#  ['0', '0', '0', '0', '0'],
#  ['1', '0', '1', '0', '1'],
#  ['0', '0', '0', '0', '0'],
#  ['1', '0', '1', '0', '1']]

for r in range(w):
    for c in range(h):
        if r+1 == w or c+1 == h:
            break
        w = matrix[r][c]
        x = matrix[r][c+1]
        y = matrix[r+1][c]
        z = matrix[r+1][c+1]

        temp = w+x+y+z


pprint(matrix)
