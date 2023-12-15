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

ans = 0

for i, line in enumerate(d) :
    for j, char in enumerate(line) :
        if char != 'O' :
            continue        
        cur = i
        while cur -1 >= 0 and d[cur-1][j] == '.' :
            d[cur][j] = '.'
            d[cur-1][j] = 'O'
            cur = cur -1
        ans += len(d)-cur
print(ans)


