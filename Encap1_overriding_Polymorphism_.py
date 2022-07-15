#encapsulation

class no_courses:
    def __init__(self):
        self.course1='kids neuron'
    def kids(self):
        print(self.course1)
object=no_courses()
object.kids()
object.course1='Tech neuron'
object.kids()

class affiliates:
    def __init__(self):
        self.__affiliate='thousand students'
    def students(self):
        print(self.__affiliate)
    def students_new(self,new):
        self.__affiliate=new
object1=affiliates()
object1.students()
object1.__affiliates='Lakh students'
object1.students_new(' Lakh studens')
object1.students()



class number_of_courses:
    def student(self):
        print("FSDS student")
    def success_story(self):
        print("printing success_story ")

# Overriding
class Java_marathon(number_of_courses):
    def student(self):
        print("java marathon student")

j=  number_of_courses()
j.student()

k=Java_marathon()
k.student()



#Polymorphism
class  course:
    def ML_DL(self):
        print('This is  ML_DL blog')
class Devops:
    def ML_DL(self):
        print('This is ML_DL course')
def polymorphism(a):
    a.ML_DL()
m=course()
n=Devops()
polymorphism(m)
polymorphism(n)