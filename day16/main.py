from collections import deque

graph = open(0).read().splitlines()

N = len(graph)
M = len(graph[0])

key = []
vis = [[0] * M for _ in range(N)]

q = deque()
 #   0  1  2  3
dr = [-1, 0, 1, 0]
dc = [ 0, 1, 0,-1]

q.append((0,0,1))
while q :
    R,C,D = q.popleft()
    
    if R < 0 or C < 0 or R >= N or C >= M :
        continue
    if (R,C,D) in key :
        continue

    vis[R][C] = 1
    key.append((R,C,D))
    if graph[R][C] == '|' :
        if D == 1 or D == 3 :
            q.append((R+dr[0], C+dc[0], 0))
            q.append((R+dr[2], C+dc[2], 2))
        else :
            q.append((R+dr[D], C+dc[D],D))
    elif graph[R][C] == '-' :
        if D == 0 or D == 2 :
            q.append((R+dr[1], C+dc[1], 1))
            q.append((R+dr[3], C+dc[3], 3))
        else :
            q.append((R+dr[D], C+dc[D],D))
    elif graph[R][C] == '/' :
        if D == 0 :
            q.append((R+dr[1],C+dc[1],1))
        if D == 1 :
            q.append((R+dr[0],C+dc[0],0))
        if D == 2 :
            q.append((R+dr[3],C+dc[3],3))
        if D == 3 :
            q.append((R+dr[2],C+dc[2],2))
    elif graph[R][C] == '\\':
        if D == 0 :
            q.append((R+dr[3],C+dc[3],3))
        if D == 1 :
            q.append((R+dr[2],C+dc[2],2))
        if D == 2 :
            q.append((R+dr[1],C+dc[1],1))
        if D == 3 :
            q.append((R+dr[0],C+dc[0],0))
    else :
        q.append((R+dr[D], C+dc[D],D))

ans = 0
for i in vis :
    for j in i :
        if j == 1 :
            ans += 1
    print(i)
print(ans)