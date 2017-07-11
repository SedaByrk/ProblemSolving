def fibonacci(limit):
    numbers = [1, 2]
    y = numbers[0] + numbers[1]
    while y < int(limit):
        y = (int(numbers[len(numbers)-1])+int(numbers[len(numbers)-2]))
        if(y < int(limit)):
            numbers.append(y)
    return(numbers)


def addition(numb):
    sum = 0
    numbers = fibonacci(numb)
    for i in range(len(numbers)):
        if(numbers[i] % 2 == 0):
            sum += numbers[i]
    print(sum)

addition(4000000)
