# 닭이 길을 건너간 이유는 과학적으로 깊게 연구가 되어 있지만, 의외로 소가 길을 건너간 이유는 거의 연구된 적이 없다. 이 주제에 관심을 가지고 있었던 농부 존은 한 대학으로부터 소가 길을 건너는 이유에 대한 연구 제의를 받게 되었다.

# 존이 할 일은 소가 길을 건너는 것을 관찰하는 것이다. 존은 소의 위치를 N번 관찰하는데, 각 관찰은 소의 번호와 소의 위치 하나씩으로 이루어져 있다. 존은 소를 10마리 가지고 있으므로 소의 번호는 1 이상 10 이하의 정수고, 소의 위치는 길의 왼쪽과 오른쪽을 의미하는 0과 1 중 하나다.

# 이 관찰 기록을 가지고 소가 최소 몇 번 길을 건넜는지 알아보자. 즉 같은 번호의 소가 위치를 바꾼 것이 몇 번인지 세면 된다.
import sys
sys.stdin = open('input.txt')

N = int(input())

cow_dic = {}
cross = 0
for _ in range(N):
    a, b = map(int, input().split())
    if a not in cow_dic:
        cow_dic[a] = b
    elif a in cow_dic and b != cow_dic[a]:  # 딕셔너리에 있고, value 값이 변경이 있다면
        cow_dic[a] = b  # 그 value 값으로 변경하고 cross에 1추가
        cross += 1

print(cross)
print(cow_dic)
