import sys
sys.stdin = open("input.txt")

N = int(input())
A, B = map(int, input().split())

if N > A or N > B:
