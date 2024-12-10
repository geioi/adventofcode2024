from itertools import product

with open('input.txt') as f:
    lines = f.readlines()
    
def generatePermutations(symbols, length):
    permutations = []
    possiblePermutations = product(symbols, repeat=length)
    for permutation in possiblePermutations:
        permutations.append(list(permutation))
    return permutations
    
    
def part1(lines):
    summa = 0
    
    for line in lines:
        line = line.strip()
        jupid = line.split(':')
        targetValue = int(jupid[0])
        values = jupid[1].strip().split(' ')
        possibleOperators = generatePermutations(['+', '*'], len(values)-1)
        #print(possibleOperators)
        for possibility in possibleOperators:
            totalValue = 0
            for i in range(len(possibility)):
                if possibility[i] == '+':
                    if totalValue == 0:
                        totalValue = int(values[i]) + int(values[i+1])
                    else:
                        totalValue = totalValue + int(values[i+1])
                else:
                    if totalValue == 0:
                        totalValue = int(values[i]) * int(values[i+1])
                    else:
                        totalValue = totalValue * int(values[i+1])
            if targetValue == totalValue:
                summa += targetValue
                break
                
    return summa

def part2(lines):
    summa = 0
    
    for line in lines:
        line = line.strip()
        jupid = line.split(':')
        targetValue = int(jupid[0])
        values = jupid[1].strip().split(' ')
        possibleOperators = generatePermutations(['+', '*', '||'], len(values)-1)
        #print(possibleOperators)
        
        for possibility in possibleOperators:
            totalValue = 0
            concatenatedValue = 0
            for i in range(len(possibility)):
                if possibility[i] == '+':
                    if totalValue == 0 and concatenatedValue == 0:
                        totalValue = int(values[i]) + int(values[i+1])
                    elif concatenatedValue != 0:
                        totalValue = int(concatenatedValue) + int(values[i+1])
                        concatenatedValue = 0
                    else:
                        totalValue = totalValue + int(values[i+1])
                elif possibility[i] == '*':
                    if totalValue == 0 and concatenatedValue == 0:
                        totalValue = int(values[i]) * int(values[i+1])
                    elif concatenatedValue != 0:
                        totalValue = int(concatenatedValue) * int(values[i+1])
                        concatenatedValue = 0
                    else:
                        totalValue = totalValue * int(values[i+1])
                else:
                    if concatenatedValue != 0:
                        concatenatedValue = concatenatedValue + values[i+1]
                    else:
                        if totalValue == 0:
                            concatenatedValue = values[i] + values[i+1]
                        else:
                            concatenatedValue = str(totalValue) + values[i+1]
            
            if concatenatedValue != 0:
                totalValue = int(concatenatedValue)
            if targetValue == totalValue:
                #print('sobis: ' + line)
                summa += targetValue
                break
    return summa
    
    
#print(part1(lines))
print(part2(lines))