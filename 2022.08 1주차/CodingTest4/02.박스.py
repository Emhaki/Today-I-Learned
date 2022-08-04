from pprint import pprint
import sys
sys.stdin = open('input.txt', "r")

T = int(input())


m, n = map(int, input().split())
box_list = []
for _ in range(1):
    for _ in range(m):
        box_list.append(list(map(str, input().split())))

# box_list
# [['1', '0', '0', '0'],
#  ['0', '0', '1', '0'],
#  ['1', '0', '0', '1'],
#  ['0', '1', '0', '0'],
#  ['1', '0', '1', '0']]

# 1을 만나고 나서부터 0의 갯수
    count = 0
for i in range(m):
    for j in range(n):
        if box_list[m-1][n-1] == '1':
            if box_list[i][j] == '1':
                for k in range(n):
                    if box_list[i][k] != box_list[0][0] and box_list[i][k] == '1':
                        count += 1

        if box_list[m-1][n-1] == '0':
            if box_list[i][j] == '1':
                for k in range(n):
                    if box_list[i][k] == '0':
                        count += 1

        elif box_list[i][j] == '0':
            break

print(count)
