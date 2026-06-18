#Austin Lineberry
#February 16th, 2026
#Written for Bellevue University CIS245
#Module 9

#This is a program to accomplish the following:
#1. Prompt user for first and last name of the student.
#2. Create a student object by passing those names to __init__
#3. Create a loop to prompt user for the following:
#       >Grade >Credits for each course taken.
#4. Once the user ends the loop, display the student's cumulative GPa

class student:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.gradePoints = 0
        self.credits = 0
        self.gpa = 0

    def calcGPA(self, grade, credits):
        self.credits = self.credits + credits
        if grade == "A":
            self.gradePoints = self.gradePoints + (int(credits)*4)
        if grade == "B":
            self.gradePoints = self.gradePoints + (int(credits)*3)
        if grade == "C":
            self.gradePoints = self.gradePoints + (int(credits)*2)
        if grade == "D":
            self.gradePoints = self.gradePoints + (int(credits)*1)
        else:
            self.gradePoints = self.gradePoints + (int(credits)*0)
            
        self.gpa = (self.gradePoints)/(self.credits)

    def getGPA(self):
        print(f"The GPA for {self.firstName} is {round(self.gpa, 1)}")

#defines main method
def main() :
    import pdb
    pdb.set_trace()
    #Gets first/last name per REQ#1
    studentFirst = input("What is your first name:")   
    studentLast = input("What is your last name:")
    
    #Creates a student object by passing first and last to init method per REQ #2
    studentOne = student(studentFirst,studentLast)
    endLoop = "y"
    
    #Creates a loop to prompt for grade and credits for each course per REQ #3
    while endLoop == "y":
        tempGrade = input("Please input student LETTER grade: ")
        tempCredits = input("Please input credits earned: ")
        studentOn.calcGPA(tempGrade, int(tempCredits))
        endLoop = input("Hit y to continue entering grades, or anything to stop.")
    #prints the student's name and GPA per REQ #4    
    studentOne.getGPA()
main()

