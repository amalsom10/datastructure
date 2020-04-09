class Instagram:
    def __init__(self,name,place,interest):
        self.name = name
        self.place = place
        self.interest = interest

    def clientdetails(self):
        print ("\nName: {}\nPlace: {}\nInterest: {}". format (self.name, self.place, self.interest))


c1 = Instagram("amal", "india", "computer")
c2 = Instagram("abc", "england", "science")
c3 = Instagram("def", "ireland", "social research")
c4 = Instagram("ghi", "usa", "geography")
c5 = Instagram("jkl", "china", "electronics")
c6 = Instagram("mno", "russia", "humanilties")
c7 = Instagram("pqr", "japan", "computer")
c8 = Instagram("stu", "france", "biology")
c9 = Instagram("vwx", "italy", "histroy")
c10 = Instagram("yz", "germany", "envstudies")

c1.following = c6
c2.following = c7
c3.following = c10
c7.following = c10
c4.following = c9
c5.following = c3
c6.following = c1
c8.following = c10
c9.following = c1
c10.following = c1

print("\n--------\nFollowing List:\n------------\n")
print ("\n-----client: {}------".format(c1.name))
c1.following.clientdetails()
print ("\n-----client: {}------".format(c2.name))
c2.following.clientdetails()
print ("\n-----client: {}------".format(c3.name))
c3.following.clientdetails()
print ("\n-----client: {}------".format(c4.name))
c4.following.clientdetails()
print ("\n-----client: {}------".format(c5.name))
c5.following.clientdetails()
print ("\n-----client: {}------".format(c6.name))
c6.following.clientdetails()
print ("\n-----client: {}------".format(c7.name))
c7.following.clientdetails()
print ("\n-----client: {}------".format(c8.name))
c8.following.clientdetails()
print ("\n-----client: {}------".format(c9.name))
c9.following.clientdetails()
print ("\n-----client: {}------".format(c10.name))
c10.following.clientdetails()
