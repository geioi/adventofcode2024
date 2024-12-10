with open('input.txt') as f:
    lines = f.readlines()
   
def isInbounds(coordinate, rowCount, colCount):
    if coordinate[0] < 0 or coordinate[1] < 0 or coordinate[0] > (rowCount-1) or coordinate[1] > (colCount-1):
        return False
    return True
   
def part1(lines):
    antennaeLocs = {}
    playfield = []
    possibleAntinodeLocs = []
    for line in lines:
        playfield.append(list(line.strip()))
    #print(playfield)
    for i in range(len(playfield)):
        for j in range(len(playfield[i])):
            if playfield[i][j].isalnum():
                if playfield[i][j] not in antennaeLocs:
                    antennaeLocs[playfield[i][j]] = [[i, j]]
                else:
                    antennaeLocs[playfield[i][j]].append([i,j])
    for key in antennaeLocs.keys():
        for i in range(len(antennaeLocs[key])):
            currX = antennaeLocs[key][i][0]
            currY = antennaeLocs[key][i][1]
            for possibility in antennaeLocs[key][i+1:]:
                higherPosX = currX - (abs(currX - possibility[0]))
                if currY > possibility[1]:
                    higherPosY = currY + abs(currY - possibility[1])
                    lowerPosY = possibility[1] - (currY - possibility[1])
                else:
                    higherPosY = currY - abs(currY - possibility[1])
                    lowerPosY = possibility[1] + abs(currY - possibility[1])
                    
                lowerPosX = possibility[0] + (possibility[0] - currX)
                possibleAntinodeLocs.append([higherPosX, higherPosY])
                possibleAntinodeLocs.append([lowerPosX, lowerPosY])
    
    antiNodeLocs = []
    rowCount = len(playfield)
    colCount = len(playfield[0])
    for antinode in possibleAntinodeLocs:
        if isInbounds(antinode, rowCount, colCount):
            if antinode not in antiNodeLocs:
                antiNodeLocs.append(antinode)
    print(antiNodeLocs)
    
    #for antinodeLoc in antiNodeLocs:
    #    if not playfield[antinodeLoc[0]][antinodeLoc[1]].isalnum():
    #        playfield[antinodeLoc[0]][antinodeLoc[1]] = '#'
        
    #for row in playfield:
    #    print(row)
    return len(antiNodeLocs)

def part2(lines):
    antennaeLocs = {}
    playfield = []
    possibleAntinodeLocs = []
    for line in lines:
        playfield.append(list(line.strip()))
    
    rowCount = len(playfield)
    colCount = len(playfield[0])
    for i in range(len(playfield)):
        for j in range(len(playfield[i])):
            if playfield[i][j].isalnum():
                if playfield[i][j] not in antennaeLocs:
                    antennaeLocs[playfield[i][j]] = [[i, j]]
                else:
                    antennaeLocs[playfield[i][j]].append([i,j])
    for key in antennaeLocs.keys():
        for i in range(len(antennaeLocs[key])):
            currX = antennaeLocs[key][i][0]
            currY = antennaeLocs[key][i][1]
            
            if len(antennaeLocs[key]) > 1:
                possibleAntinodeLocs.append([currX, currY])
            for possibility in antennaeLocs[key][i+1:]:
                possibleAntinodeLocs.append([possibility[0], possibility[1]])
                distanceX = abs(currX - possibility[0])
                distanceY = abs(currY - possibility[1])
                if currY > possibility[1]:
                    YisHigher = True
                else:
                    YisHigher = False
                
                #push x axis higher
                currentCoords = [currX, currY]
                while currentCoords[0] > 0 and currentCoords[1] > 0 and currentCoords[1] < colCount:
                    higherPosX = currentCoords[0] - distanceX
                    if YisHigher:
                        higherPosY = currentCoords[1] + distanceY
                    else:
                        higherPosY = currentCoords[1] - distanceY
                    possibleAntinodeLocs.append([higherPosX, higherPosY])
                    currentCoords = [higherPosX, higherPosY]
                #push x axis lower
                currentCoords = [possibility[0], possibility[1]]
                while currentCoords[0] < rowCount and currentCoords[1] > 0 and currentCoords[1] < colCount:
                    lowerPosX = currentCoords[0] + distanceX
                    if YisHigher:
                        lowerPosY = currentCoords[1] - distanceY
                    else:
                        lowerPosY = currentCoords[1] + distanceY
                    possibleAntinodeLocs.append([lowerPosX, lowerPosY])
                    currentCoords = [lowerPosX, lowerPosY]
    
    antiNodeLocs = []
    for antinode in possibleAntinodeLocs:
        if isInbounds(antinode, rowCount, colCount):
            if antinode not in antiNodeLocs:
                antiNodeLocs.append(antinode)
    #print(antiNodeLocs)
    
    #for antinodeLoc in antiNodeLocs:
    #    if not playfield[antinodeLoc[0]][antinodeLoc[1]].isalnum():
    #        playfield[antinodeLoc[0]][antinodeLoc[1]] = '#'
        
    #for row in playfield:
    #    print(''.join(row))
    return len(antiNodeLocs)

#print(part1(lines))
print(part2(lines))