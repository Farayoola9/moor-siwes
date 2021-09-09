# Class
# Build a student class
class Students:

    def __init__(self, name, age, gender, matric_no):
        self.name = name
        self.age = age
        self.gender = gender
        self.matric_no = matric_no
        self.level = "ND I"

        print(f"My name is {self.name}, I am a student of Fcahptib")

    def payFees(self):
        print(f"{self.name} has paid the amount of 57,000")

student1 = Students("Aishat", 21, "F", "NDCOM/19/344")
student2 = Students("Maryam", 13, "F", "NDSLT/30/5437")

print(student1.name)
print(student2.gender)

student1.payFees()

#Inheritance
class PartTimeStudents(Students):
    def __init__(self, name, age, gender, matric_no):
        Students.__init__(self, name, age, gender, matric_no)

    def payFees(self):
        print(f"{self.name} has paid the amount of 257,000")


pt_student = PartTimeStudents("Aishat", 65, "F", "344")
pt_student.payFees()

#polymorphism
