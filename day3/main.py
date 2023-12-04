
## part 1
# file = open(0).read().rsplit()

# rowSize = len(file)
# colSize = len(file[0])

# color = [[0 for _ in range(colSize)]for _ in range(rowSize)]

# dr = [-1,-1,-1,0,1,1,1,0]
# dc = [-1,0,1,1,1,0,-1,-1]

# for r, line in enumerate(file) :
#     for c, char in enumerate(line) :
#         if char.isdigit() == False and char != '.' :
#             for d in range (0,8) :
#                 nr = r+dr[d]
#                 nc = c+dc[d]
#                 if nr < 0 or nc < 0 or nr >= rowSize or nc >= colSize :
#                     continue
#                 color[nr][nc] = 1

# ans = 0

# for r, line in enumerate(file) :
#     num = 0
#     flag = 0
#     for c, char in enumerate(line) :
#         if char.isdigit() == True :
#             num *= 10
#             num += int(char)
#             if color[r][c] == 1 :
#                 flag = 1

#         if char.isdigit() == False or c+1 == colSize :
#             if flag == 1 :
#                 ans += num
#                 print(num)
#             num = 0
#             flag = 0
# print(ans)


## part 2
file = open(0).read().rsplit()

rowSize = len(file)
colSize = len(file[0])


dr = [-1,-1,-1,0,1,1,1,0]
dc = [-1,0,1,1,1,0,-1,-1]

cache = set()

for r, line in enumerate(file) :
    for c, char in enumerate(line) :
        if char == '*' :
            cache.add((r,c))

ans = 0
for (r, c) in cache:
    color = [[0 for _ in range(colSize)]for _ in range(rowSize)]
    calculator = []

    for d in range(0, 8):
        nr = r + dr[d]
        nc = c + dc[d]
        if nr < 0 or nc < 0 or nr >= rowSize or nc >= colSize:
            continue
        color[nr][nc] = 1

    for i, line in enumerate(file):
        num = 0
        flag = 0
        for j, char in enumerate(line):
            if char.isdigit():
                num *= 10
                num += int(char)
                if color[i][j] == 1:
                    flag = 1
            if not char.isdigit() or j + 1 == colSize:
                if flag == 1:
                    calculator.append(num)
                num = 0
                flag = 0

    if len(calculator) == 2:
        ans += calculator[0] * calculator[-1]

print(ans)
