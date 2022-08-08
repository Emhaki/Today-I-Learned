# 한상덕은 이번에 중덕 고등학교에 새로 부임한 교장 선생님이다. 교장 선생님으로서 첫 번째 일은 각 반의 수학 시험 성적의 통계를 내는 일이다.

# 중덕 고등학교 각 반의 학생들의 수학 시험 성적이 주어졌을 때, 최대 점수, 최소 점수, 점수 차이를 구하는 프로그램을 작성하시오.
import sys
sys.stdin = open('input.txt')

K = int(input())

for _ in range(1, K+1):
    list_ = []  # 숫자를 담을 리스트
    Lasrgest_gap = 0  # 인접한 큰 값
    list_ = list(map(int, input().split()))
    list_.pop(0)  # 필요없는 성적 갯수 삭제 [5, 30, 25, 76, 23, 78]
    list_.sort()  # [23, 25, 30, 76, 78]
    for i in range(len(list_)-1):  # 인덱스 보다 1 작게 탐색
        if abs(list_[i]-list_[i+1]) >= Lasrgest_gap:  # 인덱스 0과 1의 차
            Lasrgest_gap = abs(list_[i]-list_[i+1])  # 조건이 맞다면 그게 최대 값

    print(f'Class {_}')
    print(f'Max {max(list_)}, Min {min(list_)}, Largest gap {Lasrgest_gap}')
