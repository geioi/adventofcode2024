import re

with open('input.txt') as f:
    lines = f.readlines()

def part1(lines):
    summa = 0
    for line in lines:
        results = re.findall("mul\(\d+,\d+\)", line)
        for res in results:
            jupid = res.split('mul(')[1].split(',')
            esimeneNr = int(jupid[0])
            teineNr = int(jupid[1][:-1])
            summa += esimeneNr * teineNr
    return summa

def part2(lines):
    summa = 0
    do = True
    for line in lines:
        results = re.findall("do\(\)|don't\(\)|mul\(\d+,\d+\)", line)
        for res in results:
            if res == "do()":
                do = True
            elif res == "don't()":
                do = False
            else:
                if do:
                    jupid = res.split('mul(')[1].split(',')
                    esimeneNr = int(jupid[0])
                    teineNr = int(jupid[1][:-1])
                    summa += esimeneNr * teineNr
    return summa

#print(part1(lines))
print(part2(lines))