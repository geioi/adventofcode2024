with open('input.txt') as f:
    lines = f.readlines()
    
def part1(lines):
    originalLine = []
    for line in lines:
        originalLine = list(line.strip())
    
    formedLine = []
    isFreeSpace = False
    currIdx = 0
    for nr in originalLine:
        if not isFreeSpace:
            for i in range(int(nr)):
                formedLine.append(str(currIdx))
            currIdx += 1
            isFreeSpace = True
        else:
            for i in range(int(nr)):
                formedLine.append('.')
            isFreeSpace = False
    
    positions = {}
    for i in range(len(formedLine)):
        if formedLine[i] in positions:
            positions[formedLine[i]].append(i)
        else:
            positions[formedLine[i]] = [i]
    
    availablePositions = positions['.']
    del positions['.']
    reversedPositions = dict(reversed(list(positions.items())))
    
    modifiedLine = formedLine.copy()
    for key, values in reversedPositions.items():
        values.reverse()
        for idx in values:
            if len(availablePositions) > 0 and availablePositions[0] < idx:
                modifiedLine[availablePositions[0]] = key
                modifiedLine[idx] = '.'
                availablePositions.pop(0)
    
    checksum = 0
    for i in range(len(modifiedLine)):
        if modifiedLine[i] != '.':
            checksum += i * int(modifiedLine[i])
    
    return checksum

def part2(lines):
    originalLine = []
    for line in lines:
        originalLine = list(line.strip())
    
    formedLine = []
    isFreeSpace = False
    currIdx = 0
    for nr in originalLine:
        if not isFreeSpace:
            for i in range(int(nr)):
                formedLine.append(str(currIdx))
            currIdx += 1
            isFreeSpace = True
        else:
            for i in range(int(nr)):
                formedLine.append('.')
            isFreeSpace = False
    #print(''.join(formedLine))
    
    positions = {}
    for i in range(len(formedLine)):
        if formedLine[i] in positions:
            positions[formedLine[i]].append(i)
        else:
            positions[formedLine[i]] = [i]
    #print(positions)
    
    availablePositions = positions['.']
    del positions['.']
    reversedPositions = dict(reversed(list(positions.items())))
    #print(reversedPositions)
    #print(availablePositions)
    
    spaceLengths = {}
    previousNr = False
    continuousCount = 0
    firstIdx = False
    lastIdx = False
    for nr in availablePositions:
        if previousNr is False:
            continuousCount = 1
            firstIdx = nr
        else:
            if nr - previousNr == 1:
                continuousCount += 1
            else:
                if str(continuousCount) in spaceLengths:
                    spaceLengths[str(continuousCount)].append(firstIdx)
                else:
                    spaceLengths[str(continuousCount)] = [firstIdx]
                continuousCount = 1
                firstIdx = nr
        if availablePositions.index(nr) == len(availablePositions)-1:
            if str(continuousCount) in spaceLengths:
                    spaceLengths[str(continuousCount)].append(firstIdx)
            else:
                spaceLengths[str(continuousCount)] = [firstIdx]
        previousNr = nr
    #print(spaceLengths)
        
    modifiedLine = formedLine.copy()
    for key, values in reversedPositions.items():
        #print('checking key: ' + key)
        neededSpace = len(values)
        usableSpaces = []
        for space in spaceLengths.keys():
            if int(space) >= neededSpace:
                usableSpaces.append(space)
        if (len(usableSpaces)):
            lowestIdx = False
            earliestKey = False
            for usableSpace in usableSpaces:
                if not lowestIdx:
                    lowestIdx = spaceLengths[str(usableSpace)][0]
                    earliestKey = str(usableSpace)
                else:
                    if spaceLengths[str(usableSpace)][0] < lowestIdx:
                        lowestIdx = spaceLengths[str(usableSpace)][0]
                        earliestKey = str(usableSpace)
            
            if lowestIdx < values[0]:
                leftover = int(earliestKey) - neededSpace
                i = 0
                while i < neededSpace:
                    modifiedLine[lowestIdx + i] = key
                    i += 1
                for value in values:
                    modifiedLine[value] = '.'
                spaceLengths[earliestKey].pop(0)
                if len(spaceLengths[earliestKey]) == 0:
                    del spaceLengths[earliestKey]
                if leftover > 0:
                    if str(leftover) in spaceLengths:
                        spaceLengths[str(leftover)].append(lowestIdx+i)
                        spaceLengths[str(leftover)].sort()
                    else:
                        spaceLengths[str(leftover)] = [lowestIdx+i]
        #print(''.join(modifiedLine))
    
    checksum = 0
    for i in range(len(modifiedLine)):
        if modifiedLine[i] != '.':
            checksum += i * int(modifiedLine[i])
    
    return checksum

print(part1(lines))
print(part2(lines))