# # part 1
# d = open(0).read()

# inst, node = d.split("\n\n")
# node = node.splitlines()
# # print(node)

# mmap = {}

# for x in node :
#     u, v = x.split(" = ")
#     v = v[1:-1].split(", ")
#     mmap[u] = v

# # print(inst)
# # print(mmap)

# cur = 'AAA'
# idx = 0
# ans = 0
# while cur != 'ZZZ' :
#     direction = 0 if inst[idx] == 'L' else 1
#     cur = mmap[cur][direction]
#     idx = (idx+1) % len(inst)
#     ans += 1

# print(ans)

# # part 2 Brute force

# d = open(0).read()

# inst, node = d.split("\n\n")
# node = node.splitlines()
# # print(node)

# mmap = {}
# cur = []

# for x in node :
#     u, v = x.split(" = ")
#     v = v[1:-1].split(", ")
#     if u[-1] == 'A' :
#         cur.append(u)
#     mmap[u] = v

# idx = 0
# ans = 0
# z_cnt = 0

# while z_cnt != len(cur) :
#     nxt_cur = []
#     z_cnt = 0
#     direction = 0 if inst[idx] == 'L' else 1

#     for c in cur :
#         nxt_cur.append(mmap[c][direction])
#         if mmap[c][direction][-1] == 'Z' :
#             z_cnt += 1
#     idx = (idx+1) % len(inst)
#     ans += 1
#     cur = nxt_cur

# print(ans)

# # part 2 lcm 

import math

d = open(0).read()

inst, node = d.split("\n\n")
node = node.splitlines()

mmap = {}
cur = []

for x in node :
    u, v = x.split(" = ")
    v = v[1:-1].split(", ")
    if u[-1] == 'A' :
        cur.append(u)
    mmap[u] = v

def n_step(cur) :
    count = 0
    while cur[-1] != 'Z' :
        direction = 0 if inst[count % len(inst)] == 'L' else 1
        cur = mmap[cur][direction]
        count += 1
    return count

outputs = [n_step(c) for c in cur]
print(outputs)

ans = math.lcm(*outputs)
print(ans)

# not generalizable solution
# maybe CRT ??