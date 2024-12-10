with open('input.txt') as f:
    lines = f.readlines()

def part1(lines):
    safeCounter = 0
    for line in lines:
        jupid = line.split()
    
        isAscending = None
        lastNr = None
        
        for i in range(len(jupid)):
            jupp = int(jupid[i])
            if lastNr == None:
                lastNr = jupp
            else:
                if abs(lastNr - jupp) < 1 or abs(lastNr - jupp) > 3:
                    break
                
                if isAscending == None:
                    if jupp > lastNr:
                        isAscending = True
                        lastNr = jupp
                    else:
                        isAscending = False
                        lastNr = jupp
                elif isAscending and jupp < lastNr:
                    break
                elif not isAscending and jupp > lastNr:
                    break
                else:
                    if len(jupid)-1 == i:
                        #print(line)
                        safeCounter += 1
                    else:
                        lastNr = jupp
    return safeCounter


def part2_2(lines):
    safeCounter = 0
    safe = []
    notsafe = []
    #lines = ['45 48 44 42 40 37\n', '41 44 40 39 36 37\n']
    for line in lines:
        jupid = line.split()
    
        isSafe = False
        possibilities = []
        for i in range(len(jupid)):
            newList = jupid.copy()
            newList.pop(i)
            possibilities.append(newList)
        
        isSafe = False
        for possibility in possibilities:
            if isSafe:
                break
            isAscending = None
            lastNr = None
            for i in range(len(possibility)):
                jupp = int(possibility[i])
                if lastNr == None:
                    lastNr = jupp
                else:
                    if abs(lastNr - jupp) < 1 or abs(lastNr - jupp) > 3:
                        break
                    
                    if isAscending == None:
                        if jupp > lastNr:
                            isAscending = True
                            lastNr = jupp
                        else:
                            isAscending = False
                            lastNr = jupp
                    elif isAscending and jupp < lastNr:
                        break
                    elif not isAscending and jupp > lastNr:
                        break
                    else:
                        if len(possibility)-1 == i:
                            #print(line)
                            isSafe = True
                        else:
                            lastNr = jupp
            
        if isSafe:
            safe.append(line)
            safeCounter += 1
        else:
            notsafe.append(line)

    #print(safe)
    #print(notsafe)
    return safeCounter

#print(str(part1(lines)))
print(str(part2_2(lines)))
                    