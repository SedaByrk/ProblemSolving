import math

count = 1
j = 3
while(count < 10001):
    for i in range(3, int(math.sqrt(j)+1), 2):
        if(j % i == 0):
            break
    else:
        count += 1
    j += 2

print(j - 2)
