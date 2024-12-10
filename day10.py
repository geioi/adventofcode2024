from copy import deepcopy

with open('input.txt') as f:
    lines = f.readlines()

def findNextTrail(topoMap, row, column, lastvalue, isFirst, isPart2):
    currValue = topoMap[row][column]
    # have we already visited this location?
    if len(topoMap[row][column]) > 1:
        return 0
    if currValue == '&' or currValue == '.':
        return 0
    if int(currValue) != 0 and int(currValue) - lastvalue != 1:
        return 0
    if int(currValue) == 0 and (lastvalue != 0 or not isFirst):
        return 0
    if int(currValue) == 9:
        if not isPart2:
            topoMap[row][column] += ';'
        return 1
    if not isPart2:
        # ; stands for "visited already" to avoid dupe entries
        topoMap[row][column] += ';'
    return findNextTrail(topoMap, row + 1, column, int(currValue), False, isPart2) + findNextTrail(topoMap, row - 1, column, int(currValue), False, isPart2) + findNextTrail(topoMap, row, column + 1, int(currValue), False, isPart2) + findNextTrail(topoMap, row, column - 1, int(currValue), False, isPart2)

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
    topoMap = createPadding(lines)
    #for trail in topoMap:
    #    print(''.join(trail))
        
    totalHikingTrails = 0
    topoMapCopy = deepcopy(topoMap)
    for i in range(len(topoMap)):
        for j in range(len(topoMap[i])):
            if topoMap[i][j] == '0':
                totalHikingTrails += findNextTrail(topoMapCopy, i, j, int(topoMapCopy[i][j]), True, False)
                #reset the map
                topoMapCopy = deepcopy(topoMap)
    return totalHikingTrails

def part2(lines):
    topoMap = createPadding(lines)
    #for trail in topoMap:
    #    print(''.join(trail))
        
    totalHikingTrails = 0
    topoMapCopy = deepcopy(topoMap)
    for i in range(len(topoMap)):
        for j in range(len(topoMap[i])):
            if topoMap[i][j] == '0':
                totalHikingTrails += findNextTrail(topoMapCopy, i, j, int(topoMapCopy[i][j]), True, True)
                #reset the map
                topoMapCopy = deepcopy(topoMap)
    return totalHikingTrails

print(part1(lines))
print(part2(lines))