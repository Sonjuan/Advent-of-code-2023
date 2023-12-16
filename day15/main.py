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
    

d = open(0).read().rstrip().split(',')

ans = 0

for line in d :
    cur = 0
    for char in line :
        cur += ord(char)
        cur *= 17
        cur %= 256
    ans += cur
print(ans)

