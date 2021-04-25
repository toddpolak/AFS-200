def even(val):
    if(int(val) % 2 == 0):
        return True
    return False

def multOfFour(val):
    if(int(val) % 4 == 0):
        return True
    return False

def evenDiv(val1, val2):
    if(int(val1) % int(val2) == 0):
        return True
    return False

def project1():
    num = input("Enter a number: ")

    if(multOfFour(num)):
        print(num + " is a multiple of 4.")
    elif(even(num)):
        print("You entered an even number.")
    else:
        print("You entered an odd number.")

    num = input("Enter a number: ")
    check = input("Enter a second number: ")

    if(evenDiv(num, check)):
        print(check + " divides evently into " + num)
    else:
        print(check + " does not divide evently into " + num)

project1()