class user():
    def userInfo(self):
        name = input("Enter your name: ")
        print("Hello, " + name.upper())

def getUserInfo():
    curUser = user()
    curUser.userInfo()

getUserInfo()