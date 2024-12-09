from toolkit import *

lines = GetStringLines('./adventOfCode2024/day03.sample')
lines = GetStringLines('./adventOfCode2024/day03.input')

def part1():
    
    res = 0
    for line in lines:
        x = line
        print(x)
        startIdx = x.index("mul(")

        for ch in range(startIdx, len(x)):
            try:
                endIdx = x.index(")", startIdx)
            except:
                break

            #print (x.index("mul("))
            #print (x.index(")", startIdx))
            s = ""
            for i in range(startIdx+4, endIdx):
                s += str(x[i])
                args = s.split(",")
            #print(s)
            isValid = False
            try:
                if (len(args)==2 and int(args[0])>=1 and int(args[0])<=999 and int(args[1])>=1 and int(args[1])<=999):
                    isValid = True
            except:
                isValid = False
            if (isValid):
                res += int(args[0]) * int(args[1])
                #print("Valid index at: " + str(startIdx) + " | " + str(args[0]) + "," + str(args[1]))
                startIdx = startIdx + (endIdx - startIdx + 1)
            else:
                startIdx += 1
            #print("New startIndex: " + str(startIdx))
            if ((startIdx + 8) > len(x)):
                break
        print("Result: " + str(res))

    return None
part1()