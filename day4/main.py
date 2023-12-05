# # part 1

# d = open(0).read().splitlines()

# ans = 0

# for line in d :
    
#     left = line.split(": ")[1].split(" | ")[0].lstrip(' ').split()

#     winNums = set()
#     for num in left :
#         winNums.add(num)
    
#     right = line.split(" | ")[1].lstrip(' ').split()
    
#     point = 0
#     for num in right :
#         for win in winNums :
#             if num == win :
#                 if point == 0 :
#                     point |= 1
#                 else :
#                     point <<= 1
#     ans += point
# print (ans)

# # part2

d = open(0).read().splitlines()

N = int(d[-1].split(":")[0].split()[-1])
ans = 0
table = [0] * (N+1)

for i in range(1,N+1) :
    table[i] = 1

for line in d :
    gameID = int(line.split(":")[0].split()[-1])
    left = line.split(": ")[1].split(" | ")[0].lstrip(' ').split()

    winNums = set()
    for num in left :
        winNums.add(num)
    
    right = line.split(" | ")[1].lstrip(' ').split()
    
    point = 0
    for num in right :
        for win in winNums :
            if num == win :
                point += 1

    for p in range(gameID+1, gameID+1+point):
        table[p] += 1*table[gameID]

ans = sum(table)
print(ans)