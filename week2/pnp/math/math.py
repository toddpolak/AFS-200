from math import pi

def circleArea(radius):
    return pi * int(radius)**2

rad = float(input("Enter the radius of a circle: "))

print("The area of a circle with radius " + str(rad) + " is: " + str(circleArea(rad)))