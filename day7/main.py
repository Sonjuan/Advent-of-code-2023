# # first ordering : type
# # second ordering : stronger first card? stronger second card? ...
# # part 1

# d = open(0).read().splitlines()

# # 중복된 원소를 찾아 마킹한다
# typeOfKind = [[] for _ in range(7)] 

# for line in d :
#     card, bid = line.split()
#     table = {}
#     for char in card :
#         if char in table : 
#             table[char] += 1
#         else :
#             table[char] = 1
    
#     sorted_table = sorted(table.items(), key=lambda item: item[1], reverse=True)
    
#     if int(sorted_table[0][1]) == 5 :
#         typeOfKind[0].append((card,bid))
#     elif int(sorted_table[0][1]) == 4 :
#         typeOfKind[1].append((card,bid))
#     elif int(sorted_table[0][1]) == 3 and int(sorted_table[1][1]) == 2 :
#         typeOfKind[2].append((card,bid))
#     elif int(sorted_table[0][1]) == 3 :
#         typeOfKind[3].append((card,bid))
#     elif int(sorted_table[0][1]) == 2 and int(sorted_table[1][1]) == 2 :
#         typeOfKind[4].append((card,bid))
#     elif int(sorted_table[0][1]) == 2 :
#         typeOfKind[5].append((card,bid))
#     else :
#         typeOfKind[6].append((card,bid))

# ans = 0
# rank = len(d)
# order = "AKQJT98765432"
# for pairs in typeOfKind :
#     if len(pairs) == 0 :
#         continue
#     pairs = sorted(pairs, key=lambda word : [order.index(c) for c in word[0]])
#     for el in pairs :
#         print(el, rank)
#         ans += int(el[1]) * rank
#         rank -= 1
# print(ans)


# part 2
d = open(0).read().splitlines()

# 중복된 원소를 찾아 마킹한다
typeOfKind = [[] for _ in range(7)] 

for line in d :
    card, bid = line.split()
    table = {}
    wild = 0
    
    for char in card :
        if char in table : 
            table[char] += 1
        else :
            table[char] = 1
        
    if 'J' in table :
        wild = table['J']
        table['J'] = 0

    sorted_table = sorted(table.items(), key=lambda item: item[1], reverse=True)

    if wild != 0 :
        x, y = sorted_table[0]
        sorted_table[0] = (x,y+wild)


    if int(sorted_table[0][1]) == 5 :
        typeOfKind[0].append((card,bid))
    elif int(sorted_table[0][1]) == 4 :
        typeOfKind[1].append((card,bid))
    elif int(sorted_table[0][1]) == 3 and int(sorted_table[1][1]) == 2 :
        typeOfKind[2].append((card,bid))
    elif int(sorted_table[0][1]) == 3 :
        typeOfKind[3].append((card,bid))
    elif int(sorted_table[0][1]) == 2 and int(sorted_table[1][1]) == 2 :
        typeOfKind[4].append((card,bid))
    elif int(sorted_table[0][1]) == 2 :
        typeOfKind[5].append((card,bid))
    else :
        typeOfKind[6].append((card,bid))

ans = 0
rank = len(d)
order = "AKQT98765432J"
for pairs in typeOfKind :
    if len(pairs) == 0 :
        continue
    pairs = sorted(pairs, key=lambda word : [order.index(c) for c in word[0]])
    for el in pairs :
        # print(el, rank)
        ans += int(el[1]) * rank
        rank -= 1
print(ans)

