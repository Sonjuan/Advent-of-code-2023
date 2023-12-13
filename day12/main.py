# # part 1 
# d = open(0).read().splitlines()


# def recur(records, target) :

#     if records == "" :
#         return 1 if len(target) == 0 else 0
#     if len(target) == 0 :
#         return 0 if '#' in records else 1

#     if records[0] ==  '.' :
#         return recur(records[1:], target)

#     if records[0] == '#' :
#         if target[0] <= len(records) and '.' not in records[:target[0]] and (target[0] == len(records) or records[target[0]] != '#') :
#             return recur(records[target[0]+1:], target[1:])
#         else :
#             return 0

#     if records[0] == '?' :
#         return recur('.'+records[1:], target) + recur('#'+records[1:], target)

# ans = 0
# for line in d :
#     records, info = line.split()
#     info = list(map(int, info.split(',')))
#     ans += recur(records, info)
#     print(ans)


# part 2
d = open(0).read().splitlines()

cache = {}

def recur(records, target) :
    if records == "" :
        return 1 if len(target) == 0 else 0
    if len(target) == 0 :
        return 0 if '#' in records else 1

    key = (records, target)
    if key in cache :
        return cache[key]
    result = 0

    if records[0] ==  '.' :
        result += recur(records[1:], target)

    if records[0] == '#' :
        if target[0] <= len(records) and '.' not in records[:target[0]] and (target[0] == len(records) or records[target[0]] != '#') :
            result += recur(records[target[0]+1:], target[1:])
        else :
            result += 0

    if records[0] == '?' :
        result += recur('.'+records[1:], target) + recur('#'+records[1:], target)
    
    cache[key] = result
    return result

ans = 0
for line in d :
    records, info = line.split()
    info = tuple(map(int, info.split(',')))
    records = '?'.join([records] * 5)
    info = info*5
    ans += recur(records, info)

    print(ans)
