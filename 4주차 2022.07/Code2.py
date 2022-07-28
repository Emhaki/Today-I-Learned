# 사람의 수 입력
N = int(input())

list_ = []

# 각 사람의 몸무게와 키 입력
for i in range(N):
    weight, height = list(map(int, input().split()))
    # 리스트에 몸무게와 키를 저장
    list_.append((weight, height))

ranks = [0] * N

# 모든 사람을 비교하기위한 이중반복문
for a in range(N):
    # 기준이 되는 사람
    A = list_[a]
    for b in range(N):
        # 비교가 되는 사람
        B = list_[b]

        # A가 B보다 덩치가 큰지 조건문이 필요
        # A가 B보다 덩치가 크다.
        if A[0] > B[0] and A[1] > B[1]:
            # B보다 덩치가 큰 사람이 한 명 더 있다. +1
            ranks[b] += 1

for rank in ranks:
    print(rank+1, end=" ")
