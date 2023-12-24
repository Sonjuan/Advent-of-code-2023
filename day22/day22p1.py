file = open(0).read().splitlines()

tower = []

for line in file :
    st, en = line.split('~')
    st = list(map(int,st.split(',')))
    en = list(map(int, en.split(',')))
    tower.append(st+en)

tower.sort(key=lambda z : z[2])

def overlaps(a,b) :
    return max(a[0],b[0]) <= min(a[3],b[3]) and max(a[1],b[1]) <= min(a[4],b[4])

for i, brick in enumerate(tower) :
    max_z = 1
    for check in tower[:i] :
        if overlaps(brick, check) :
            max_z = max(max_z, check[5]+1)
    brick[5] -= brick[2] - max_z
    brick[2] = max_z

tower.sort(key=lambda x : x[2])

up = {i:set() for i in range(len(tower))}
down = {i:set() for i in range(len(tower))}

for j, upper in enumerate(tower) :
    for i, lower in enumerate(tower[:j]) :
        if overlaps(lower,upper) and upper[2] == lower[5]+1 :
            up[i].add(j)
            down[j].add(i)

ans = 0

for i in range(len(tower)) :
    if all(len(down[j]) >= 2 for j in up[i]) :
        ans += 1

print(ans)
