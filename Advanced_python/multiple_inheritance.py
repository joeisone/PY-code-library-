class Father():
    def skills(self):
        print("Accounting,painting")

class Mother():
    def skills(self):
        print("Coding,Cooking")


class child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("sports")

c=child()
c.skills()

#Exercise
class teacher():
     def profession(self):
         print('I am a teacher')

class student(teacher):
    def profession(self):
        print('I am a student')

class YouTuber(student):
    def profession(self):
        teacher.profession(self)
        student.profession(self)
        print('I am a Youtuber')

Y=YouTuber()
Y.profession()

