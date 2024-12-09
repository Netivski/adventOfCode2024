from toolkit import *

lines = GetStringLines('./adventOfCode2024/day02.input')
lines = GetStringLines('./adventOfCode2024/day02.sample')

def part1():
    isValidCount = 0
    for line in lines:
        levels = line.split(' ')
        isIncreasing = int(levels[0]) < int(levels[1])
        isValid = False
        #print(levels)
        for i in range(0, len(levels)-1):
            currLevel = int(levels[i])
            nextLevel = int(levels[i+1])
            #print("CurrLevel:" + str(currLevel) + " | NextLevel:" + str(nextLevel))
            if (isIncreasing):
                if ((currLevel>nextLevel) or (nextLevel-currLevel < 1) or (nextLevel-currLevel > 3)):
                    break
            if (not(isIncreasing)):
                if ((nextLevel>currLevel) or (currLevel-nextLevel < 1) or (currLevel-nextLevel > 3)):
                    break
            if (i+2 == len(levels)):
                isValid = True
        if (isValid): isValidCount += 1
        #break   
    print("Valid reports:" + str(isValidCount))
    return None


def part2():
    isValidCount = 0
    for line in lines:
        levels = line.split(' ')
        isIncreasing = int(levels[0]) < int(levels[1])
        isValid = False
        isTolerant = True
        #print(levels)
        for i in range(0, len(levels)-1):
            currLevel = int(levels[i])
            nextLevel = int(levels[i+1])
            #print("CurrLevel:" + str(currLevel) + " | NextLevel:" + str(nextLevel))
            if (isIncreasing):
                if ((currLevel>nextLevel) or (nextLevel-currLevel < 1) or (nextLevel-currLevel > 3)):
                    if (isTolerant):
                        isTolerant = False
                    else:
                        break
            if (not(isIncreasing)):
                if ((nextLevel>currLevel) or (currLevel-nextLevel < 1) or (currLevel-nextLevel > 3)):
                    if (isTolerant):
                        isTolerant = False
                    else:
                        break
            if (i+2 == len(levels)):
                isValid = True
        if (isValid): isValidCount += 1
        #break   
    print("Valid reports:" + str(isValidCount))
    return None

#part1()
part2()