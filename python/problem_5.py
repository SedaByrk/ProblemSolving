mult1 = 1


def leastCommonMultiple(numb1, numb2):
    global mult1
    numb = max(numb1, numb2)
    if(numb > 1):
        for i in range(2, numb + 1):
            if(numb1 % i == 0 and numb2 % i == 0):
                mult1 = mult1 * i
                leastCommonMultiple(int(numb1 / i), int(numb2 / i))
                break
            elif(numb1 % i == 0 and numb2 % i != 0):
                mult1 = mult1 * i
                leastCommonMultiple(int(numb1 / i), numb2)
                break
            elif(numb1 % i != 0 and numb2 % i == 0):
                mult1 = mult1 * i
                leastCommonMultiple(numb1, int(numb2 / i))
                break
    return(mult1)


mult = leastCommonMultiple(20, 19)
for i in range(18, 1, -1):
    mult1 = 1
    mult = leastCommonMultiple(mult, i)
print(mult)
