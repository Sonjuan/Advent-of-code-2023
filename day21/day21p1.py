from collections import deque

file = open(0).read().splitlines()

N = len(file)
M = len(file[0])

sr, sc = next( (r,c) for r, row in enumerate(file) for c, ch in enumerate(row) if ch =='S'  )

dr = [0,0,1,-1]
dc = [-1,1,0,0]

ans = []
vis = {(sr,sc)}

q = deque()
q.append((sr,sc,0))

while q :
    R, C, step = q.popleft()

    if step > 64 :
        continue

    if step % 2 == 0 :
        ans.append((R,C))    
    
    for k in range(4) :
        nr, nc = R + dr[k], C + dc[k]
        if nr < 0 or nc < 0 or nr >= N or nc >= M :
            continue

        if file[nr][nc] == '#' :
            continue

        if (nr,nc) in vis :
            continue

        vis.add((nr,nc))
        q.append((nr,nc,step+1))
print(len(ans))