from collections import deque

file = open(0).read().splitlines()

N = len(file)
M = len(file[0])
sr = 0
sc = 0

for i, line in enumerate(file) :
    for j, ch in enumerate(line) :
        if ch == 'S' :
            sr, sc = i, j

dr = [0,0,1,-1]
dc = [-1,1,0,0]

cache = [(sr,sc,0)]
vis = [(sr,sc)]

q = deque()
q.append((sr,sc,0))

while q :
    R, C, step = q.popleft()

    for k in range(4) :
        nr = R + dr[k]
        nc = C + dc[k]
        if nr < 0 or nc < 0 or nr >= N or nc >= M :
            continue
        if file[nr][nc] == '#' :
            continue
        if (nr,nc) in vis :
            continue
        if step+1 > 64 :
            continue
        vis.append((nr,nc))
        cache.append((nr,nc,step+1))
        q.append((nr,nc,step+1))

ans = 0
for i in cache :
    r,c,step = i
    if step % 2 == 0 :
        ans += 1
print(ans)