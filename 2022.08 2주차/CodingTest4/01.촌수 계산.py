import sys
sys.stdin = open("input.txt")


def pprint(arr):
    for i in range(len(arr)):
        print(i, arr[i])


n = int(input())
start, end = list(map(int, input().split()))

m = int(input())

# 빈 리스트를 (n+1)개를 가진 이차원 리스트
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    # 공백을 기준으로 2개의 숫자가 입력되기 때문에
    x, y = list(map(int, input().split()))  # 스필릿과 맵을 이용해 정수로 변환

    # 무방향 인접 그래프이기 때문에
    graph[x].append(y)
    graph[y].append(x)

# graph
# 0 []
# 1 [2, 3]
# 2 [1, 7, 8, 9]
# 3 [1]
# 4 [5, 6]
# 5 [4]
# 6 [4]
# 7 [2]
# 8 [2]
# 9 [2]

# 방문 표시를 할 리스트
visited = [False] * (n + 1)
# visited
# 0 False
# 1 False
# 2 False
# 3 False
# 4 False
# 5 False
# 6 False
# 7 False
# 8 False
# 9 False

# dfs를 시작하기위해서 기본값 설정
# stack = [start]
stack = []
stack.append((start, 0))
visited[start] = True

# 정답을 출력할 변수
answer = -1

# 스택이 비어있지 않으면 반복
while len(stack) != 0:
    # LIFO, 스택의 가장 위에 있는 값을 저장
    # 번호와 촌수를 같이 pop
    number, count = stack.pop()

    # pop을 한 값이 우리가 원하는 값(end)
    # 촌수가 연결이 안되어있으면 이 아래구문은 실행 x
    if number == end:
        answer = count
        break

    # 해당하는 값의 인접 그래프를 저장
    adj_graph = graph[number]
    # print(number, adj_graph)

    # 인접하는 값들을 탐색
    for adj_number in adj_graph:
        # 방문한적이 없을 때만 스택에 값을 append
        if not visited[adj_number]:
            # 인접 번호와 촌수를 같이 append
            stack.append((adj_number, count + 1))
            # 인접 값을 방문 표시
            visited[adj_number] = True

# 촌수를 계산하려면
print(count)
