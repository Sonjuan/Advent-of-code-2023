# # part 1
# d = open(0).read().splitlines()

# ans = 0

# for line in d :
#     line = list(map(int, line.split()))
#     table = []
#     table.append(line)
    
#     while True :
#         newTable = []
#         zeros = 0
#         for i in range(1, len(table[-1])) :
#             if table[-1][i] - table[-1][i-1] == 0 :
#                 zeros += 1
#             newTable.append(table[-1][i]-table[-1][i-1])
#         if zeros == len(newTable) :
#             break

#         table.append(newTable)

#     for l in reversed(table) :
#         ans += l[-1]
# print(ans)

# part 2
d = open(0).read().splitlines()

ans = 0

for line in d :
    line = list(map(int, line.split()))
    table = []
    table.append(line)
    
    while True :
        newTable = []
        zeros = 0
        for i in range(1, len(table[-1])) :
            if table[-1][i] - table[-1][i-1] == 0 :
                zeros += 1
            newTable.append(table[-1][i]-table[-1][i-1])
        if zeros == len(newTable) :
            break

        table.append(newTable)

    prev = 0
    for l in reversed(table) :
        prev = l[0] - prev
    ans += prev

print(ans)