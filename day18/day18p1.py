# part 1

file = open(0).read().splitlines()
    #  0  1  2  3
dr = [-1, 0, 1, 0]
dc = [ 0, 1, 0,-1]

R = 1500
C = 1500

graph = [[0] * 3000 for _ in range(3000)]

outer = 0
for line in file :
    D, L, code = line.split()
    
    if D == 'U' :
        direction = 0
    if D == 'R' :
        direction = 1
    if D == 'D' :
        direction = 2
    if D == 'L' :
        direction = 3
    
    for _ in range(int(L)) :
        R = R + dr[direction] 
        C = C + dc[direction]
        graph[R][C] = 1
        outer += 1

q = []
def bfs() :
    while q :
        r, c = q.pop()
        for k in range(4) :
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nc < 0 or nr >= 3000 or nc >= 3000 :
                continue
            if graph[nr][nc] != 0 :
                continue
            graph[nr][nc] = 1
            q.append((nr,nc))

q.append((0,0))
bfs()

inner = 0
for i in range(3000) :
    for j in range(3000) :
        if graph[i][j] == 0 :
            inner += 1

print(inner + outer)




