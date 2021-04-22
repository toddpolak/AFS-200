def oddOrEven(val):
    if(int(val) % 2 == 0):
        print("You entered an even number.")
    else:
        print("you entered an odd number.")

def multOfFour(val):
    if(int(val) % 4 == 0):
        return True
    return False

def evenDiv(val1, val2):
    if(int(val1) % int(val2) == 0):
        print(val2 + " divides evently into " + val1)
    else:
        print(val2 + " does not divide evently into " + val1)

num = input("Enter a number: ")

if(multOfFour(num)):
    print("Your number is a multiple of 4.")
else:
    oddOrEven(num)

num = input("Enter a number: ")
check = input("Enter a second number: ")

evenDiv(num, check)