with open('input.txt') as f:
    lines = f.readlines()
    
def part1(lines):
    for line in lines:
        jupid = line.strip().split(' ')
        print(jupid)
        updated_arr = []
        for i in range(25):
            for nr in jupid:
                if nr == '0':
                    updated_arr.append('1')
                elif len(nr) % 2 == 0:
                    leftNr = nr[0:len(nr) // 2].lstrip('0')
                    rightNr = nr[len(nr) // 2:].lstrip('0')
                    if leftNr == '':
                        leftNr = '0'
                    if rightNr == '':
                        rightNr = '0'
                    updated_arr.append(leftNr)
                    updated_arr.append(rightNr)
                else:
                    updated_arr.append(str(int(nr) * 2024))
            jupid = updated_arr.copy()
            updated_arr = []
            #print(jupid)
        
        #print(updated_arr)
        print(len(jupid))
    return len(jupid)

def part2(lines):
    for line in lines:
        jupid = line.strip().split(' ')
        nrsInList = {}
        for nr in jupid:
            if nr in nrsInList:
                nrsInList[nr] += 1
            else:
                nrsInList[nr] = 1
        updated_arr = []
        for i in range(75):
            for key, value in nrsInList.copy().items():
                if value != 0:
                    if key == '0':
                        if '1' in nrsInList:
                            nrsInList['1'] += (1 * value)
                        else:
                            nrsInList['1'] = (1 * value)
                        nrsInList[key] -= (1 * value)
                    elif len(key) % 2 == 0:
                        leftNr = key[0:len(key) // 2].lstrip('0')
                        rightNr = key[len(key) // 2:].lstrip('0')
                        if leftNr == '':
                            leftNr = '0'
                        if rightNr == '':
                            rightNr = '0'
                        if leftNr in nrsInList:
                            nrsInList[leftNr] += (1 * value)
                        else:
                            nrsInList[leftNr] = (1 * value)
                        if rightNr in nrsInList:
                            nrsInList[rightNr] += (1 * value)
                        else:
                            nrsInList[rightNr] = (1 * value)
                        nrsInList[key] -= (1 * value)
                    else:
                        calculated = str(int(key) * 2024)
                        if calculated in nrsInList:
                            nrsInList[calculated] += (1 * value)
                        else:
                            nrsInList[calculated] = (1 * value)
                        nrsInList[key] -= (1 * value)
        totalLen = 0
        for value in nrsInList.values():
            totalLen += value

    return totalLen

#print(part1(lines))
print(part2(lines))