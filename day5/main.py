# # part1
# seeds, *blocks = open(0).read().split("\n\n")

# seeds = list(map(int,seeds.split(":")[1].split()))


# for block in blocks :
#     ranges = []
#     for line in block.splitlines()[1:] :
#         ranges.append(list(map(int, line.split())))

#     new = []
    
#     for x in seeds :
#         for a, b, c in ranges :
#             if x in range(b, b+c) :
#                 new.append(x - b + a)
#                 break
#         else :
#             new.append(x)

#     seeds = new

# print(min(seeds))

# # part2
inputs, *blocks = open(0).read().split("\n\n")

inputs = list(map(int,inputs.split(":")[1].split()))

seeds = []
for i in range(0, len(inputs), 2) :
    seeds.append((inputs[i], inputs[i] + inputs[i+1]))

for block in blocks :
    ranges = []
    for line in block.splitlines()[1:] :
        ranges.append(list(map(int, line.split())))

    new = []
    
    while len(seeds) > 0 :
        s, e = seeds.pop()
        for a, b, c in ranges :
            os = max(s, b)
            oe = min(e, b + c)
            if os < oe :
                new.append((os-b+a, oe-b+a))
                if os > s :
                    seeds.append((s,os))
                if e > oe :
                    seeds.append((oe,e))
                break
        else :
            new.append((s,e))
    seeds = new
print(min(seeds)[0])