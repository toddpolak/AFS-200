

multiplier = 360

multiply = lambda x: x * multiplier

print(multiply (5))

def func_compute(n):
    return lambda x : x * n

result = func_compute(2)

print(result(15))