# part 1
# sum = 0

# for line in open(0):
#     print(line)
#     v = ''
#     for char in line:
#         if char.isdigit() == True :
#             v += char
#     v = v[0] + v[-1]
#     sum += int(v)

# print(sum)

#part 2

sum = 0

for line in open(0):
    line = line.rstrip()
    v = ''
    for i, char in enumerate(line):
        if char.isdigit() == True :
            v += char
        else :
            for j, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']) :
                if line[i:].startswith(val) :
                    v += str((j+1))
    v = v[0] + v[-1]
    sum += int(v)

print(sum)

