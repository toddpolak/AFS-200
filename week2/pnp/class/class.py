class user():
    def userInfo(self):
        fName = input("Enter your first name: ")
        lName = input("Enter your last name: ")
        print("Hello, " + fName.upper() + " " + lName.upper())

def getUserInfo():
    curUser = user()
    curUser.userInfo()

getUserInfo()