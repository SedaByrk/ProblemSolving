def xy():
    c = 5
    addition = 3 + 4 + 5
    while(c < addition):
        for b in range(4, c):
            for a in range(3, b):
                if a**2 + b**2 == c**2:
                    if 1000 % (a + b + c) == 0:
                        x = (1000 / (a + b + c))
                        return(a * x * b * x * c * x)
        c += 1
        addition = a + b + c
print(xy())
