numb = []


def primeNumbers(number):
    for j in range(2, number+1):
        if(number % j == 0):
            for i in range(2, j):
                if(j % i == 0):
                    break
            else:
                if(j not in numb):
                    numb.append(j)
                    primeNumbers(int(number/j))
                else:
                    return(max(numb))
print(primeNumbers(600851475143))
