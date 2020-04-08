# basic class program
class students:
    def __int__(self, name, classdivision, rollnumber)
        self.name = name
        self.classdivision = classdivision
        self.rollnumber = rollnumber

    def studentdetails(self):
        print ("My name is %s \n I am studying in %s \n My rollnumber is %s" . format (self.name, self.classdivision, self.rollnumber))




s1 = students("abc", "2a", 13)
s2 = students("def", "10a", 20)

s1.studentdetails()
s2.studentdetails()
