
# d = open(0).read().splitlines()

# src = (0,0)
# N = len(d)
# M = len(d[0])

# for i,v in enumerate(d) :
#     for j,k in enumerate(v) :
#         if d[i][j] == 'S' :
#             src = (i,j)
#     # 0  1 2  3
# dr = [-1, 0,1,0]
# dc = [ 0, 1, 0,-1]
# vis = set()
# step = 0
# ans = 0

# # suppose K is direction North East South West
# def Route(pos) :
#     R, C, K = pos
#     if d[R][C] == '.':
#         return False
#     elif d[R][C] == '|' :
#         if K == 0 or K == 2 :
#             return True
#     elif d[R][C] == '-' :
#         if K == 1 or K == 3 :
#             return True
#     elif d[R][C] == 'L' :
#         if K == 0 or K == 1 :
#             return True
#     elif d[R][C] == 'J' :
#         if K == 0 or K == 3 :
#             return True
#     elif d[R][C] == '7' :
#         if K == 3 or K == 2 :
#             return True
#     elif d[R][C] == 'F' :
#         if K == 1 or K == 2 :
#             return True
#     elif d[R][C] == 'S' :
#         return True
#     return False

# def opp(k) :
#     if k == 0 :
#         return 2
#     if k == 2 :
#         return 0
#     if k == 1 :
#         return 3
#     if k == 3 :
#         return 1

# def search(pos) :
#     global step

#     for k in range(0,4) :
#         nr = pos[0] + dr[k]
#         nc = pos[1] + dc[k]
#         if nr < 0 or nc < 0 or nr >= N or nc >= M :
#             continue
#         if (nr,nc,opp(k)) in vis:
#             continue
#         if Route((nr,nc,opp(k))) == False:
#             continue 
#         if d[nr][nc] == 'S' :
#             global ans
#             print(step)
#             ans = max(ans, (step+1)//2)
#             continue
#         vis.add((pos[0],pos[1],k))
#         vis.add((nr,nc,opp(k)))
#         step += 1
#         search((nr,nc, opp(k)))
#         vis.remove((pos[0],pos[1],k))
#         vis.remove((nr,nc,opp(k)))
#         step -= 1


# search((src[0],src[1],-1))

# print(ans)
# # cannot take backtrack approach

# part 1

# from collections import deque

# grid = open(0).read().strip().splitlines()

# for r, row in enumerate(grid):
#     for c, ch in enumerate(row):
#         if ch == "S":
#             sr = r
#             sc = c
#             break
#     else:
#         continue
#     break

# loop = {(sr, sc)}
# q = deque([(sr, sc)])

# while q:
#     r, c = q.popleft()
#     ch = grid[r][c]

#     if r > 0 and ch in "S|JL" and grid[r - 1][c] in "|7F" and (r - 1, c) not in loop:
#         loop.add((r - 1, c))
#         q.append((r - 1, c))
        
#     if r < len(grid) - 1 and ch in "S|7F" and grid[r + 1][c] in "|JL" and (r + 1, c) not in loop:
#         loop.add((r + 1, c))
#         q.append((r + 1, c))

#     if c > 0 and ch in "S-J7" and grid[r][c - 1] in "-LF" and (r, c - 1) not in loop:
#         loop.add((r, c - 1))
#         q.append((r, c - 1))

#     if c < len(grid[r]) - 1 and ch in "S-LF" and grid[r][c + 1] in "-J7" and (r, c + 1) not in loop:
#         loop.add((r, c + 1))
#         q.append((r, c + 1))
    
#     print(loop)

# print(len(loop) // 2)

# # there is just two connected parts and src 'S' is on the loop, it is just linear iteration

d = open(0).read().splitlines()

N = len(d)
M = len(d[0])

r,c = 0,0
for i,v in enumerate(d) :
    for j,k in enumerate(v) :
        if d[i][j] == 'S' :
            r, c = i, j

dr = [-1, 0, 1,0]
dc = [0,  1, 0,-1]
k = 0

for i in range(0,4) :
    nr = r +dr[i]
    nc = c +dc[i]
    if nr < 0 or nc < 0 or nr >= N or nc >= M :
        continue
    if i==0 and d[nr][nc] in '.-LJ' :
        continue
    if i==1 and d[nr][nc] in '.|FL' :
        continue
    if i==2 and d[nr][nc] in '.-F7' :
        continue
    if i==3 and d[nr][nc] in '.|J7' :
        continue
    r = nr
    c = nc
    k = i
    break

def Route(r,c,k) :
    if d[r][c] == '|' :
        if k == 0 :
            return 2
        else :
            return 0
    
    if d[r][c] == '-' :
        if k == 1 :
            return 3
        else :
            return 1
        
    if d[r][c] == 'L' :
        if k == 0 :
            return 1
        else :
            return 0
        
    if d[r][c] == 'J' :
        if k == 0 :
            return 3
        else :
            return 0
        
    if d[r][c] == '7' :
        if k == 3 :
            return 2
        else :
            return 3
    if d[r][c] == 'F' :
        if k == 1 :
            return 2
        else :
            return 1
        
def opp(k) :
    if k==0 : return 2
    if k==1 : return 3
    if k==2 : return 0
    if k==3 : return 1

step = 1
while d[r][c] != 'S' :
    k = opp(k)
    k = Route(r,c,k)
    r = r + dr[k]
    c = c + dc[k]
    step += 1

print(step//2)