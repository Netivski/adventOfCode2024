from toolkit import *

#lines = GetStringLines('./adventOfCode2024/day01.sample')
lines = open('./adventOfCode2024/day01.input').readlines()

def part1():
    listA = []
    listB = []
    listC = []
    res = 0
    for line in lines:
        l = line.split("   ")
        listA.append(int(l[0]))
        listB.append(int(l[1]))
    listA.sort()
    listB.sort()
    for i in range(0, len(listA)):
        res += abs(listA[i]-listB[i])
        listC.append(abs(listA[i]-listB[i]))
        print(str(listA[i]) + " - " + str(listB[i]) + ' = ' + str(abs(listA[i]-listB[i])))
    print(res)

def part2():
    listA = []
    listB = dict[int, int]()
    for line in lines:
        l = line.split("   ")
        listA.append(int(l[0]))
        if (int(l[1]) in listB.keys()):
            listB[int(l[1])] += 1
        else:
            listB[int(l[1])] = 1
    res = 0
    for v in listA:
        if (v in listB.keys()):
            res += v * listB[v]
    print ("Result: " + str(res))
    return None

#part1()
part2()
