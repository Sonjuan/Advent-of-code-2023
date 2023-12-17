# # part 1

# d = open(0).read().rstrip().split(',')

# ans = 0

# for line in d :
#     cur = 0
#     for char in line :
#         cur += ord(char)
#         cur *= 17
#         cur %= 256
#     ans += cur
# print(ans)
    
# # part 2

import re
from collections import defaultdict

d = open(0).read().rstrip().split(',')


def hashing(str) :
    ans = 0
    for char in str :
        ans = ((ans + ord(char)) * 17) % 256
    return ans


regex = r'(\w+)(=|-)(\d+)?'
labels = defaultdict(list)
lenses = defaultdict(list)

for line in d :
    for label, op, focal_len in re.findall(regex, line) :
        hash = hashing(label)

        if label in labels[hash] :
            idx = labels[hash].index(label)
            if op == '-' :
                labels[hash].pop(idx)
                lenses[hash].pop(idx)
            else :
                lenses[hash][idx] = int(focal_len)
        elif op == '=' :
            labels[hash].append(label)
            lenses[hash].append(int(focal_len))
    
ans = 0

for box, lenses in lenses.items() :
    for i, focal_len in enumerate(lenses, start=1) :
        ans += (box+1) * i * focal_len
print(ans)