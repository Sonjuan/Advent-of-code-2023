# import re
# from collections import defaultdict

# file = open(0).read()

# workflows, parts = file.split('\n\n')
# workflows = workflows.splitlines()

# table = defaultdict(int)

# # make topology sort
# for wf in workflows :
#     name, conds = wf.split('{')
#     # what the fuck
#     table[name] = table[name]

#     conds = conds[:-1].split(',')
#     for cond in conds :
#         nxt = cond.split(':')
#         if nxt[-1] in 'AR' :
#             continue
        
#         table[nxt[-1]] += 1
#         print(nxt[-1], table[nxt[-1]])

block1, block2 = open(0).read().split("\n\n")

workflows = {}

for line in block1.splitlines():
    name, rest = line[:-1].split("{")
    rules = rest.split(",")
    workflows[name] = ([], rules.pop())
    for rule in rules:
        comparison, target = rule.split(":")
        key = comparison[0]
        cmp = comparison[1]
        n = int(comparison[2:])
        workflows[name][0].append((key, cmp, n, target))

ops = {
    ">": int.__gt__,
    "<": int.__lt__
}

def accept(item, name = "in"):
    if name == "R":
        return False
    if name == "A":
        return True

    rules, fallback = workflows[name]
    
    for key, cmp, n, target in rules:
        if ops[cmp](item[key], n):
            return accept(item, target)
    
    return accept(item, fallback)

total = 0

for line in block2.splitlines():
    item = {}
    for segment in line[1:-1].split(","):
        ch, n = segment.split("=")
        item[ch] = int(n)
    if accept(item):
        total += sum(item.values())

print(total)