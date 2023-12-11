# # part 1
# d = open(0).read().splitlines()

# N = len(d)
# M = len(d[0])

# rows = [0] * N
# cols = [0] * M

# q = []

# for i in range(0,N) :
#     for j in range(0,M) :
#         if d[i][j] == '#' :
#             break
#     else :
#         rows[i] = 1

# for j in range(0,M) :
#     for i in range(0,N) :
#         if d[i][j] =='#' :
#             break
#     else :
#         cols[j] = 1

# for i in range(0,N) :
#     for j in range(0,M) :
#         if d[i][j] == '#' :
#             q.append((i,j))

# ans = 0
# for i in range(0, len(q)) :
#     for j in range(i+1, len(q)) :
#         r1, c1 = q[i]
#         r2, c2 = q[j]

#         if r1 > r2 :
#             r1, r2 = r2, r1
#         if c1 > c2 :
#             c1, c2 = c2, c1
        
#         ans += (r2-r1) + (c2-c1)
        
#         for rr in range(r1, r2+1) :
#             if rows[rr] :
#                 ans += 1
#         for cc in range(c1, c2+1) :
#             if cols[cc] :
#                 ans += 1

# print(ans)
        
# # part 2
d = open(0).read().splitlines()

N = len(d)
M = len(d[0])

rows = [0] * N
cols = [0] * M

q = []

for i in range(0,N) :
    for j in range(0,M) :
        if d[i][j] == '#' :
            break
    else :
        rows[i] = 1

for j in range(0,M) :
    for i in range(0,N) :
        if d[i][j] =='#' :
            break
    else :
        cols[j] = 1

for i in range(0,N) :
    for j in range(0,M) :
        if d[i][j] == '#' :
            q.append((i,j))

ans = 0
for i in range(0, len(q)) :
    for j in range(i+1, len(q)) :
        r1, c1 = q[i]
        r2, c2 = q[j]

        if r1 > r2 :
            r1, r2 = r2, r1
        if c1 > c2 :
            c1, c2 = c2, c1
        
        ans += (r2-r1) + (c2-c1)
        
        for rr in range(r1, r2+1) :
            if rows[rr] :
                ans += 1000000 -1
        for cc in range(c1, c2+1) :
            if cols[cc] :
                ans += 1000000 -1

print(ans)
        