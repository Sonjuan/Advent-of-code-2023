# # part 1
# d = open(0)

# ans = 0;

# for line in d :
#     line = line.rstrip()

#     gameID = line.split(":")[0].split(" ")[-1]
#     pockets = line.split(": ")[1:][0].split("; ")

#     color_counts = {'red': 12, 'blue': 14, 'green': 13}

#     for trial in pockets :
#         for balls in trial.split(", ") :
#             cnt, color = balls.split(" ")
#             if(int(cnt) > color_counts[color]) :
#                 gameID = '0';
    
#     ans += int(gameID)
# print(ans)


# part 2
d = open(0)
ans = 0;

for line in d :
    line = line.rstrip()

    pockets = line.split(": ")[1:][0].split("; ")
    color_counts = {'red': 0, 'blue': 0, 'green': 0}

    for trial in pockets :
        for balls in trial.split(", ") :
            cnt, color = balls.split(" ")
            color_counts[color] = max(color_counts[color], int(cnt));

    # print(color_counts['red']*color_counts['blue']*color_counts['green'])
    ans += color_counts['red']*color_counts['blue']*color_counts['green']
    
print(ans)
