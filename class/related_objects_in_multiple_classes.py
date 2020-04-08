class Students:
    def __init__(self, name, classdivision, rollnumber):
        self.name = name
        self.classdivision = classdivision
        self.rollnumber = rollnumber

    def studentdetails(self):
        print ("------------\nStudent info\n----------------\nName: {}\nclassdivision: {}\nrollnumber: {}". format(self.name, self.classdivision, self.rollnumber))

s1 = Students("s1", "2a", 13)
s2 = Students("s2" , "10b", 10)


class Teacher:
    """docstring for Teacher."""

    def __init__(self, name, education, isworking):
        self.name = name
        self.education = education
        self.isworking = isworking

    def teacherdetails(self):
        print ("------------\nTeacher info\n----------------\nName: {}\neducation: {}\nisworking: {}". format(self.name, self.education, self.isworking))

    def teacher_present(self):
        self.isworking = True

    def teacher_notpresent(self):
        self.isworking = False

t1 = Teacher("t1", "btech", True)
t2 = Teacher("t2", "mtech", False)

print ("\n--------\nStudent List\n------------")
s1.studentdetails()
s2.studentdetails()


print ("\n--------\nTeacher List\n-------------")
t1.teacherdetails()
t2.teacherdetails()


t1.studentlist = s1
t2.studentlist = s2

print("\n-----------\nStudents under Teachers\n----------\n")
print("Teacher: {}". format(t1.name))
t1.studentlist.studentdetails()


print("\nTeacher: {}". format(t2.name))
t2.studentlist.studentdetails()
