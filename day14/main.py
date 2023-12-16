# # part 1

# d = list(map(list,open(0).read().splitlines()))

# ans = 0

# for i, line in enumerate(d) :
#     for j, char in enumerate(line) :
#         if char != 'O' :
#             continue
        
#         cur = i
#         while cur -1 >= 0 and d[cur-1][j] == '.' :
#             d[cur][j] = '.'
#             d[cur-1][j] = 'O'
#             cur = cur -1
        
#         ans += len(d)-cur
# print(ans)

# # part 2 

d = list(map(list,open(0).read().splitlines()))
graph = d

def tilt(d) :
    for i, line in enumerate(d) :
        for j, char in enumerate(line) :
            if char != 'O' :
                continue
            cur = i
            while cur -1 >= 0 and d[cur-1][j] == '.' :
                d[cur][j] = '.'
                d[cur-1][j] = 'O'
                cur = cur -1
    return d

def rotate(graph) :
    N = len(graph)
    M = len(graph[0])
    NG = [['X' for _ in range(N)] for _ in range(M)]
    for r in range(N) :
        for c in range(M) :
            NG[c][N-1-r] = graph[r][c]
    return NG

def score(graph) :
    ans = 0
    for i, line in enumerate(graph) :
        for j, _ in enumerate(line) :
            if graph[i][j] == 'O' :
                ans += len(graph) - i
    return ans

cache = {}
limit = 10**9
t = 0

while t < limit :
    t += 1
    for _ in range(4) :
        graph = tilt(graph)
        graph = rotate(graph)

    key = tuple(tuple(row) for row in graph)    
    if key in cache :
        cycle = t - cache[key]
        dup = (limit-t) // cycle
        t += dup * cycle
    cache[key] = t

print(score(graph))