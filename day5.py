with open('input.txt') as f:
    lines = f.readlines()
    
def part1(lines):
    left_side = []
    right_side = []
    updates = []
    valid_lines = []
    summa = 0
    for line in lines:
        if (len(line) > 3):
            if line[2] == '|':
                jupid = line.split('|')
                left_side.append(jupid[0])
                right_side.append(jupid[1].strip())
            else:
                updates.append(line.strip())
    
    for update in updates:
        valid = True
        update = update.split(',')
        for i in range(len(update)):
            current_nr = update[i]
            if current_nr in right_side:
                for j in range(len(right_side)):
                    if right_side[j] == current_nr:
                        searchable = left_side[j]
                        for nr in update[i+1:]:
                            if nr == searchable:
                                valid = False
                                break
        if valid:
            summa += int(update[len(update) // 2])
            valid_lines.append(update)
                              
    return summa

def helper(left_side, right_side, update):
    valid = True
    for i in range(len(update)):
        current_nr = update[i]
        if current_nr in right_side:
            for j in range(len(right_side)):
                if right_side[j] == current_nr:
                    searchable = left_side[j]
                    for k in range(len(update)):
                        if update[k] == searchable:
                            if k > i:
                                valid = False
                                replaceable = update[i]
                                before = update.copy()
                                update[i] = update[k]
                                update[k] = replaceable
                                    #print(i)
                                    #print(k)
                                print('applied rule: ' + left_side[j] + '|' + right_side[j] + ' - '+ str(before) + ' -> ' + str(update))
                                return [valid, update]
            
    return [valid, update]

def part2(lines):
    left_side = []
    right_side = []
    updates = []
    not_valid_lines = []
    summa = 0
    for line in lines:
        if (len(line) > 3):
            if line[2] == '|':
                jupid = line.split('|')
                left_side.append(jupid[0])
                right_side.append(jupid[1].strip())
            else:
                updates.append(line.strip())
    
    for update in updates:
        valid = True
        was_valid = False
        update = update.split(',')
        while was_valid == False:
            was_valid, update = helper(left_side, right_side, update)
            if not was_valid:
                valid = False
            if was_valid and not valid:
                summa += int(update[len(update) // 2])
                print(update[len(update) // 2])
                not_valid_lines.append(update)
                break
                              
    return summa

#print(part1(lines))
print(part2(lines))