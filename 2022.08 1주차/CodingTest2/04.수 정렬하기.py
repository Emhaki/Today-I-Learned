# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
import sys

N = int(sys.stdin.readline())
num_list = []
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

for i in sorted(num_list):
    print(i)
