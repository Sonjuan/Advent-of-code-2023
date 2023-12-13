# # part 1 

# d = open(0).read().split("\n\n")

# def for_rows(graph) :
#     N = len(graph)
#     for fold in range(1,N) :
#         fold_step = min(fold, N-fold)
#         # print(fold, fold_step)
#         # print(graph[fold-fold_step:fold])
#         # print(graph[fold:fold+fold_step])
#         for i in range(0, fold_step) :
#             if graph[fold-fold_step:fold][i] != graph[fold:fold+fold_step][fold_step-i-1] :
#                 break
#         else :
#             return fold
#     return 0
    
# ans = 0
# for block in d :
#     block = block.split("\n")
#     ans += 100 * for_rows(block)

#     transposed_string = list(map(list, zip(*block)))
#     rotated_string = ["".join(row[::-1]) for row in transposed_string]
#     ans += for_rows(rotated_string)

# print(ans)

# # part 2
d = open(0).read().split("\n\n")

def for_rows(graph) :
    N = len(graph)
    for fold in range(1,N) :
        fold_step = min(fold, N-fold)
        # print(fold, fold_step)
        # print(graph[fold-fold_step:fold])
        # print(graph[fold:fold+fold_step])
        for i in range(0, fold_step) :
            if graph[fold-fold_step:fold][i] != graph[fold:fold+fold_step][fold_step-i-1] :
                break
        else :
            return fold
    return 0
    
ans = 0
for block in d :
    block = block.split("\n")
    ans += 100 * for_rows(block)

    transposed_string = list(map(list, zip(*block)))
    rotated_string = ["".join(row[::-1]) for row in transposed_string]
    ans += for_rows(rotated_string)

print(ans)
