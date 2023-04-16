import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# N 시험장 갯수, A 응시자 수
N = int(input())
A = list(map(int, input().split()))
# 총감독관 감시 응시자 수 B, 부감독관 감시 응시자 수 C
B, C = map(int, input().split())
cnt = 0

for i in range(len(A)):
    if A[i] >= B:
        A[i] -= B
        cnt += 1
        
        if A[i] % C == 0:
            cnt += (A[i] // C)
        else:
            cnt += (A[i] // C) + 1
    else:
        cnt += 1

print(cnt)
