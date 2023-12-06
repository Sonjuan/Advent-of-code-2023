# # part 1
# time, dist = open(0).read().splitlines()

# time = list(map(int, time.split(':')[1].split()))
# dist = list(map(int, dist.split(':')[1].split()))

# ans = 1

# for i, t in enumerate(time) :
#     point = 0
#     for hold in range(1, t) :
#         res = (t-hold) * hold
#         if res > dist[i] :
#             point += 1
#     ans *= point
# print(ans)

time, dist = open(0).read().splitlines()
time = int("".join(map(str, time.split(":")[1].split())))
dist = int("".join(map(str, dist.split(":")[1].split())))

point = 1
for hold in range(1,time) :
    res = (time-hold) * hold - dist
    if res > 0 :
        point += 1
    
print(point)

# equation