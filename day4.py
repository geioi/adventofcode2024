with open('input.txt') as f:
    lines = f.readlines()
    
def part1(lines):
    char_arrs = []
    for line in lines:
        char_arrs.append(list(line.strip()))
    xmas_count = 0
    for i in range(len(char_arrs)):
        for j in range(len(char_arrs[i])):
            if char_arrs[i][j] == 'X':
                #to the right check
                if len(char_arrs[i]) > j + 3:
                    if char_arrs[i][j+1] == 'M':
                        if char_arrs[i][j+2] == 'A':
                            if char_arrs[i][j+3] == 'S':
                                #print('paremale: rida ' + str(i) + ', idx:' + str(j) + '-' + str(j+3))
                                xmas_count += 1
                #to the left check
                if j - 3 > -1:
                    if char_arrs[i][j-1] == 'M':
                        if char_arrs[i][j-2] == 'A':
                            if char_arrs[i][j-3] == 'S':
                                #print('vasakule: rida ' + str(i) + ', idx:' + str(j) + '-' + str(j-3))
                                xmas_count += 1
                
                #upwards check
                if i-3 > -1:
                    if char_arrs[i-1][j] == 'M':
                        if char_arrs[i-2][j] == 'A':
                            if char_arrs[i-3][j] == 'S':
                                #print('üles: koht ' + str(j) + ', read:' + str(i) + '-' + str(i-3))
                                xmas_count += 1
                    #diagonal to up right
                    if len(char_arrs[i]) > j + 3:
                        if char_arrs[i-1][j+1] == 'M':
                            if char_arrs[i-2][j+2] == 'A':
                                if char_arrs[i-3][j+3] == 'S':
                                    #print('diagonaal üles paremale: kohad ' + str(j+3) + '-' + str(j) + ', read:' + str(i) + '-' + str(i+3))
                                    xmas_count += 1
                    
                    #diagonal to up left
                    if j-3 > -1:
                        if char_arrs[i-1][j-1] == 'M':
                            if char_arrs[i-2][j-2] == 'A':
                                if char_arrs[i-3][j-3] == 'S':
                                    #print('diagonaal üles vasakule: kohad ' + str(j-3) + '-' + str(j) + ', read:' + str(i-3) + '-' + str(i))
                                    xmas_count += 1
                                
                #downwards check
                if len(char_arrs) > i+3:
                    if char_arrs[i+1][j] == 'M':
                        if char_arrs[i+2][j] == 'A':
                            if char_arrs[i+3][j] == 'S':
                                xmas_count += 1
                    #diagonal to down right
                    if len(char_arrs[i]) > j + 3:
                        if char_arrs[i+1][j+1] == 'M':
                            if char_arrs[i+2][j+2] == 'A':
                                if char_arrs[i+3][j+3] == 'S':
                                    xmas_count += 1
                    #diagonal to down left
                    if j-3 > -1:
                        if char_arrs[i+1][j-1] == 'M':
                            if char_arrs[i+2][j-2] == 'A':
                                if char_arrs[i+3][j-3] == 'S':
                                    xmas_count += 1
    
    return(xmas_count)

def part2(lines):
    char_arrs = []
    for line in lines:
        char_arrs.append(list(line.strip()))
    x_mas_count = 0
    for i in range(len(char_arrs)):
        for j in range(len(char_arrs[i])):
            if char_arrs[i][j] == 'X':
                char_arrs[i][j] = '.'
    
    for i in range(len(char_arrs)):
        for j in range(len(char_arrs[i])):
            if char_arrs[i][j] == 'A':
                # can we look to the left and right
                if j-1 > -1 and j+1 < len(char_arrs[i]):
                    # can we look up and down
                    if i-1 > -1 and i+1 < len(char_arrs):
                        #up left and down right
                        if (char_arrs[i-1][j-1] == 'M' and char_arrs[i+1][j+1] == 'S') or (char_arrs[i-1][j-1] == 'S' and char_arrs[i+1][j+1] == 'M'):
                            # up right and down left
                            if (char_arrs[i-1][j+1] == 'M' and char_arrs[i+1][j-1] == 'S') or (char_arrs[i-1][j+1] == 'S' and char_arrs[i+1][j-1] == 'M'):
                                x_mas_count += 1
                                
    return x_mas_count
    
#print(part1(lines))
print(part2(lines))