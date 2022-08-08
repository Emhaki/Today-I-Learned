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

for x in range():

    for y in list(range())[::-1]:

        if 박스_리스트[y][x] == 박스:

            while True:

                if y+1 == 행_개수:
                    break
                if 박스_리스트[y+1][x] ==박스:
                    break
                 
                박스_리스트[y][x] = 빈공간
                박스_리스트[y+1][x] = 박스
                y += 1
                이동거리 += 1

print(이동거리)
