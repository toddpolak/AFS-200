import datetime

now = datetime.datetime.now().year

name = input("Enter your name: ")
age = input("Enter your age: ")

dif = 100 - int(age)
ans = int(now) + int(dif) 

print("Hello, " + name + ". You will turn 100 in the year: " + str(ans))
