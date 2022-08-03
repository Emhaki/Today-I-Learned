import sys
sys.stdin = open('input.txt', "r")

n, m = map(int, input().split())
array = []

for _ in range(n):
    array.append(input())

row_count, col_count = 0, 0

# 모든 행
for i in range(n):
    if 'X' not in array[i]:
        row_count += 1

# 모든 열
for j in range(m):
    if "X" not in [array[i][j] for i in range(n)]:
        col_count += 1
print(max(row_count, col_count))
