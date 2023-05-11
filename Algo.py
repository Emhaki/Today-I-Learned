import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

R, C = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(C)]
visited = [[0] * R for _ in range(C)]
queue = deque()
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(i,j, wolf):
    visited[i][j] = 1
    queue.append((i,j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < R and 0 <= ny < C and 



for i in range(R):
    for j in range(C):
        if graph[i][j] == 'v':
            bfs(i,j)