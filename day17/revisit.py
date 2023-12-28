# get the global minimum Heat using Dijkstra algorithm.
# Remember if you want to store and compare the value (in this case Heat).
# you have to think about its current state (D, S).
# So you cannot use vis[nr][nc] <= H+grid[nr][nc] or something.

import heapq

file = open(0).read().splitlines()
grid = [[int(ch)for ch in line] for line in file]

N = len(grid)
M = len(grid[0])


# 0 1 2 3
dr = [-1,0,1,0]
dc = [0,1,0,-1]

vis = set()
#H,R,C,D,Step
pq = []
heapq.heappush(pq,(0,0,0,-1,0))


while pq : 
    H,R,C,D,S = heapq.heappop(pq)
    if R == N-1 and C == M-1 :
        print(H)
        break

    if (R,C,D,S) in vis :
        continue
    vis.add((R,C,D,S))

    if S < 3 and D != -1 :
        nr = R + dr[D]
        nc = C + dc[D]
        if 0 <= nr < N and 0 <= nc < M :
            heapq.heappush(pq, (H+grid[nr][nc],nr,nc,D,S+1))

    for k in range(4) :
        if k == D :
            continue
        if D != -1 :
            if (dr[k], dc[k]) == (-dr[D],-dc[D]) :
                continue
        nr = R + dr[k]
        nc = C + dc[k]
        if nr < 0 or nc < 0 or nr >= N or nc >= M :
            continue
        heapq.heappush(pq, (H+grid[nr][nc],nr,nc,k,1))

