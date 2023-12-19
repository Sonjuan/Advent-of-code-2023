
file = open(0).read().splitlines()

#     0  1  2  3
dr = [0, 1, 0,-1]
dc = [1, 0, -1,0]

seen = []
R, C = 0, 0
outer = 0

for line in file :
    code = line.split()[-1][1:-1]
    direction = int(code[-1])
    L = int(code[1:-1], 16)

    outer += L

    R = R + L*dr[direction] 
    C = C + L*dc[direction]

    seen.append((R,C))

A = abs(sum(seen[i][0] * (seen[i - 1][1] - seen[(i + 1) % len(seen)][1]) for i in range(len(seen))  )) // 2

inner = A-outer // 2 + 1
print(inner + outer)