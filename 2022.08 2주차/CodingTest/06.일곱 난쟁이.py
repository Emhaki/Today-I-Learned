# 왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.

# 아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.

# 아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.
import sys
sys.stdin = open('input.txt')

list_ = []
for _ in range(9):
    list_.append(int(input()))
# list_ = [20, 7, 23, 19, 10, 15, 25, 8, 13]
for i in range(8):
    for j in range(i+1, 9):
        if sum(list_)-(list_[i]+list_[j]) == 100:  # i, j 가 순회하면서 100이랑 같아질 때
            x, y = i, j  # 그때의 인덱스 위치를 저장


for k in sorted(list_):  # 정렬된 리스트가
    if k != list_[x] and k != list_[y]:  # 해당값이 아닐때 출력
        print(k)
