student1FailedCourses = 2
student2FailedCourses = 0
student1Major = "physical science"
student2Major = "geography"
student1 = "Todd"
student2 = "Madeline"
student1Gender = "Male"
student2Gender = "Female"

def courseOutcome(name, gender, failed, major):
    if(failed > 0):
        if(gender=="Male"):
            genderRef = "son"
        else:
            genderRef = "daughter"
        print("Your " + genderRef + " " + name + " is failing " + str(failed) + " subjects.")
        print(name + " will need to redo " + str(failed) + " courses.")
    else:
        print(name + " is doing well in " + major + ".")


courseOutcome(student1, student1Gender, student1FailedCourses, student1Major)
courseOutcome(student2, student2Gender, student2FailedCourses, student2Major)