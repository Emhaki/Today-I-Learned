from collections import deque

N = int(input())
M = list(map(int, input().split()))

cnt = 0
queue = deque(M)
while len(queue) == 0:
    if queue.popleft() == 0:
        cnt += 1
        if queue.popleft() == 1:
            cnt = +1
            if queue.popleft() == 2:
                cnt = +1
                print(cnt)
        else:
            print(cnt)
    else:
        print(cnt)
    print(cnt)
