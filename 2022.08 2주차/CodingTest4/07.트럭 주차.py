from pprint import pprint
import sys
sys.stdin = open('input.txt')

# A 한대 B 두대 C 세대
A, B, C = map(int, input().split())

arr = [0]*100
answer = 0
print(arr)
for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        arr[i] += 1
print(arr)
for j in arr:
    answer += {0: 0, 1: A, 2: B*2, 3: C*3}[j]

print(answer)
