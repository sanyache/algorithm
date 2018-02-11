
class SchoolMember:
    count = 0
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        SchoolMember.count += 1

    def about(self):
         print('%s %s is a scool member'%(self.first_name, self.last_name))

class Teacher(SchoolMember):
    count = 0
    def __init__(self, first_name, last_name, age, subject):
        SchoolMember.__init__(self, first_name, last_name, age)
        self.subject = subject
        Teacher.count += 1

    def about(self):
        print('%s %s is a teacher of %s'%(self.first_name, self.last_name, self.subject))

class Student(SchoolMember):
    def __init__(self, first_name, last_name, age, group):
        SchoolMember.__init__(self, first_name, last_name,age)
        self.group = group
        #SchoolMember.count += 1

    def about(self):
        print ('%s %s is a student of %d group'%(self.first_name, self.last_name, self.group))

d1= SchoolMember("Mike", "Doudson",26)
print d1.count
d2= Teacher("Mark", 'Luts', 40, 'mathematics')
print d2.count
d3= Student('Tom', 'Hilfinger', 18, 22)
print d3.count
d11 = SchoolMember('Mark','Tsukerberg', 30)
print d11.count
memberList = [d1, d2, d3,d11 ]
for member in memberList:
    member.about()
    print member.count