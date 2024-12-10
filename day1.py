with open('input.txt') as f:
    lines = f.readlines()

def part1(lines):
    vasak = []
    parem = []
    summa = 0
    
    for line in lines:
        jupid = line.split()
        vasak.append(int(jupid[0]))
        parem.append(int(jupid[1]))
    
    vasak = sorted(vasak)
    parem = sorted(parem)
    
    for i in range(len(vasak)):
        summa += abs(vasak[i] - parem[i])
    
    return summa
        
        
def part2(lines):
    vasak = []
    parem = []
    summa = 0
    
    for line in lines:
        jupid = line.split()
        vasak.append(int(jupid[0]))
        parem.append(int(jupid[1]))
    
    vasak = sorted(vasak)
    parem = sorted(parem)
    
    for nr1 in vasak:
        counter = 0
        for nr2 in parem:
            if nr1 == nr2:
                counter += 1
        summa += nr1 * counter
    return summa

print(str(part1(lines)))
print(str(part2(lines)))