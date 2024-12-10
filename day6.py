from copy import deepcopy

with open('input.txt') as f:
    lines = f.readlines()

def findGuardPos(playfield):
    for i in range(len(playfield)):
        for j in range(len(playfield[i])):
            if playfield[i][j] == '^':
                return (i, j)

def createPadding(lines):
    playfield = []
    paddedRow = []
    exampleRow = lines[0].strip()
    for char in exampleRow:
        paddedRow.append('&')
    
    # add 2 more to create a complete box
    paddedRow.append('&')
    paddedRow.append('&')
    
    playfield.append(paddedRow)
    
    for line in lines:
        line = list(line.strip())
        line.insert(0, '&')
        line.append('&')
        playfield.append(line)
    playfield.append(paddedRow)
    
    return playfield

def part1(lines):
    newDirections = {'up': 'right', 'right': 'down', 'down': 'left', 'left': 'up'}
    playfield = createPadding(lines)

    #find current guard position
    guardPos = findGuardPos(playfield)
    print(guardPos)
            
    #padding created, now we can start traversing
    distinctTraversedCount = 0
    currDirection = 'up'
    while playfield[guardPos[0]][guardPos[1]] != '&':
        match currDirection:
            case 'up':
                if playfield[guardPos[0]-1][guardPos[1]] == '#':
                    currDirection = newDirections[currDirection]
                else:
                    if playfield[guardPos[0]][guardPos[1]] != 'X':
                        playfield[guardPos[0]][guardPos[1]] = 'X'
                        distinctTraversedCount += 1
                    guardPos = (guardPos[0]-1,guardPos[1])
            case 'right':
                if playfield[guardPos[0]][guardPos[1]+1] == '#':
                    currDirection = newDirections[currDirection]
                else:
                    if playfield[guardPos[0]][guardPos[1]] != 'X':
                        playfield[guardPos[0]][guardPos[1]] = 'X'
                        distinctTraversedCount += 1
                    guardPos = (guardPos[0],guardPos[1]+1)
                
            case 'down':
                if playfield[guardPos[0]+1][guardPos[1]] == '#':
                    currDirection = newDirections[currDirection]
                else:
                    if playfield[guardPos[0]][guardPos[1]] != 'X':
                        playfield[guardPos[0]][guardPos[1]] = 'X'
                        distinctTraversedCount += 1
                    guardPos = (guardPos[0]+1,guardPos[1])
                
            case 'left':
                if playfield[guardPos[0]][guardPos[1]-1] == '#':
                    currDirection = newDirections[currDirection]
                else:
                    if playfield[guardPos[0]][guardPos[1]] != 'X':
                        playfield[guardPos[0]][guardPos[1]] = 'X'
                        distinctTraversedCount += 1
                    guardPos = (guardPos[0],guardPos[1]-1)
    
    #for row in playfield:
    #    print(row)
                
    return distinctTraversedCount

def createObstruction(playfield, pos):
    new_playfield = deepcopy(playfield)
    new_playfield[pos[0]][pos[1]] = 'O'
    return new_playfield

def traversePlayfield(playfield, initialGuardPos, current):
    newDirections = {'up': 'right', 'right': 'down', 'down': 'left', 'left': 'up'}
    guardPos = deepcopy(initialGuardPos)
    
    currDirection = 'up'
    
    O_Counter = 0
    obstacleDict = {}
    # let's traverse and find if it loops, set the initial counter to 20 times before we stop the loop
    while playfield[guardPos[0]][guardPos[1]] != '&' and O_Counter <= 20:
        match currDirection:
            case 'up':
                if playfield[guardPos[0]-1][guardPos[1]] == '#' or playfield[guardPos[0]-1][guardPos[1]] == 'O':
                    currDirection = newDirections[currDirection]
                    if playfield[guardPos[0]-1][guardPos[1]] == 'O':
                        O_Counter += 1
                    if "(" + str(guardPos[0]-1) + "," + str(guardPos[1]) + ")" in obstacleDict:
                        obstacleDict["(" + str(guardPos[0]-1) + "," + str(guardPos[1]) + ")"] += 1
                    else:
                        obstacleDict["(" + str(guardPos[0]-1) + "," + str(guardPos[1]) + ")"] = 1
                    if obstacleDict["(" + str(guardPos[0]-1) + "," + str(guardPos[1]) + ")"] > 20:
                        return 1
                else:
                    guardPos = (guardPos[0]-1,guardPos[1])
                    
            case 'right':
                if playfield[guardPos[0]][guardPos[1]+1] == '#' or playfield[guardPos[0]][guardPos[1]+1] == 'O':
                    currDirection = newDirections[currDirection]
                    if playfield[guardPos[0]][guardPos[1]+1] == 'O':
                        O_Counter += 1
                    if "(" + str(guardPos[0]) + "," + str(guardPos[1]+1) + ")" in obstacleDict:
                        obstacleDict["(" + str(guardPos[0]) + "," + str(guardPos[1]+1) + ")"] += 1
                    else:
                        obstacleDict["(" + str(guardPos[0]) + "," + str(guardPos[1]+1) + ")"] = 1
                    if obstacleDict["(" + str(guardPos[0]) + "," + str(guardPos[1]+1) + ")"] > 20:
                        return 1
                else:
                    guardPos = (guardPos[0],guardPos[1]+1)
                
            case 'down':
                if playfield[guardPos[0]+1][guardPos[1]] == '#' or playfield[guardPos[0]+1][guardPos[1]] == 'O':
                    currDirection = newDirections[currDirection]
                    if playfield[guardPos[0]+1][guardPos[1]] == 'O':
                        O_Counter += 1
                    if "(" + str(guardPos[0]+1) + "," + str(guardPos[1]) + ")" in obstacleDict:
                        obstacleDict["(" + str(guardPos[0]+1) + "," + str(guardPos[1]) + ")"] += 1
                    else:
                        obstacleDict["(" + str(guardPos[0]+1) + "," + str(guardPos[1]) + ")"] = 1
                    if obstacleDict["(" + str(guardPos[0]+1) + "," + str(guardPos[1]) + ")"] > 20:
                        return 1
                else:
                    guardPos = (guardPos[0]+1,guardPos[1])
                
            case 'left':
                if playfield[guardPos[0]][guardPos[1]-1] == '#' or playfield[guardPos[0]][guardPos[1]-1] == 'O':
                    currDirection = newDirections[currDirection]
                    if playfield[guardPos[0]][guardPos[1]-1] == 'O':
                        O_Counter += 1
                    if "(" + str(guardPos[0]) + "," + str(guardPos[1]-1) + ")" in obstacleDict:
                        obstacleDict["(" + str(guardPos[0]) + "," + str(guardPos[1]-1) + ")"] += 1
                    else:
                        obstacleDict["(" + str(guardPos[0]) + "," + str(guardPos[1]-1) + ")"] = 1
                    if obstacleDict["(" + str(guardPos[0]) + "," + str(guardPos[1]-1) + ")"] > 20:
                        return 1
                else:
                    guardPos = (guardPos[0],guardPos[1]-1)
    if O_Counter < 20:
        return 0
    return 1

def part2(lines):
    newDirections = {'up': 'right', 'right': 'down', 'down': 'left', 'left': 'up'}
    playfield = createPadding(lines)

    #find current guard position
    guardPos = findGuardPos(playfield)
    initialGuardPos = deepcopy(guardPos)
    
    currDirection = 'up'
    
    # mark the initial path
    while playfield[guardPos[0]][guardPos[1]] != '&':
        match currDirection:
            case 'up':
                if playfield[guardPos[0]-1][guardPos[1]] == '#':
                    currDirection = newDirections[currDirection]
                else:
                    if playfield[guardPos[0]][guardPos[1]] != 'X':
                        playfield[guardPos[0]][guardPos[1]] = 'X'
                    guardPos = (guardPos[0]-1,guardPos[1])
            case 'right':
                if playfield[guardPos[0]][guardPos[1]+1] == '#':
                    currDirection = newDirections[currDirection]
                else:
                    if playfield[guardPos[0]][guardPos[1]] != 'X':
                        playfield[guardPos[0]][guardPos[1]] = 'X'
                    guardPos = (guardPos[0],guardPos[1]+1)
                
            case 'down':
                if playfield[guardPos[0]+1][guardPos[1]] == '#':
                    currDirection = newDirections[currDirection]
                else:
                    if playfield[guardPos[0]][guardPos[1]] != 'X':
                        playfield[guardPos[0]][guardPos[1]] = 'X'
                    guardPos = (guardPos[0]+1,guardPos[1])
                
            case 'left':
                if playfield[guardPos[0]][guardPos[1]-1] == '#':
                    currDirection = newDirections[currDirection]
                else:
                    if playfield[guardPos[0]][guardPos[1]] != 'X':
                        playfield[guardPos[0]][guardPos[1]] = 'X'
                    guardPos = (guardPos[0],guardPos[1]-1)
    #print(playfield)
    #print(initialGuardPos)
    #print(guardPos)
    possiblePlayfields = []
    for i in range(len(playfield)):
        for j in range(len(playfield[i])):
            if (i != initialGuardPos[0] or j != initialGuardPos[1]) and playfield[i][j] == 'X':
                possiblePlayfields.append(createObstruction(playfield, (i,j)))
    print('done creating lists')
    
    possibleLoops = 0
    print('list length: ' + str(len(possiblePlayfields)))
    current = 0
    print('starting loop checking')
    for option in possiblePlayfields:
        print('checking list nr ' + str(current))
        possibleLoops += traversePlayfield(option, initialGuardPos, current)
        current += 1
    return possibleLoops
    
#print(part1(lines))
print(part2(lines))