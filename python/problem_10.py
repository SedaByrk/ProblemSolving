import math

numb = 3
addition = 2

while 2000000 > numb:
    for j in range(3, int(math.sqrt(numb)+1), 2):
        if(numb % j == 0):
            break
    else:
        addition += numb
    numb += 2
print(addition)
