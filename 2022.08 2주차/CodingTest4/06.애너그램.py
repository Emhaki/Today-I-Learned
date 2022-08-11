import sys
sys.stdin = open('input.txt')

# N = int(input())
# for _ in range(N):
#     a, b = map(str, input().split())
#     # bizarre brazier
#     cnt = 0
#     cnt2 = 0
#     for i in a:
#         if i in b:
#             cnt += 1
#     for j in b:
#         if j in a:
#             cnt2 += 1
#     if cnt == len(b) and cnt2 == len(a):
#         print(f"{a} & {b} are anagrams.")
#     else:
#         print(f"{a} & {b} are NOT anagrams.")

N = int(input())

for _ in range(N):
    a, b = map(str, input().split())

    word1 = sorted(list(a))
    word2 = sorted(list(b))

    if word1 == word2:
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")