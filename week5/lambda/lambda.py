#Function that takes one argument, and that argument will be multiplied with an unknown given number

multiplier = 360

multiply = lambda x: x * multiplier

print(multiply (5))

def lambdaMultiplier(num):
    return lambda x : x * num

result = lambdaMultiplier(2)

print(result(15))