#Function that takes one argument, and that argument will be multiplied with an unknown given number

#Option 1

multiplier = 6

multiply = lambda x: x * multiplier

print(multiply (5))

#Option 2

def lambdaMultiplier(num):
    return lambda x : x * num

result = lambdaMultiplier(2)

print(result(15))