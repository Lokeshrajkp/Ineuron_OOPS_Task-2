#encapsulation
#1
import logging
logging.basicConfig(filename='encap.log',level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
class no_courses:
    logging.info('method creation inside no_courses')
    try:
      def __init__(self):
         self.course1='kids neuron'
      def kids(self):
        print(self.course1)
    except Exception as e:
        print(e)
object=no_courses()
object.kids()
object.course1='Tech neuron'
object.kids()
logging.info('#1 completed')

#2
class affiliates:
    logging.info('method creation inside no_courses')
    try:
     def __init__(self):
        self.__affiliate='thousand students'
     def students(self):
        print(self.__affiliate)
     def students_new(self,new):
        self.__affiliate=new
    except Exception as e:
        print(e)
object1=affiliates()
object1.students()
object1.__affiliates='Lakh students'
object1.students_new(' Lakh studens')
object1.students()
logging.info('#2 completed')
logging.warning('encapsulation examples completed')

# Overriding
#1
logging.info('Overriding examples in OOPS')
class number_of_courses:
    try:
       logging.info('Student method')
       def student(self):
        print("FSDS student")
       logging.info('FSDS student method')
       def success_story(self):
        logging.info('Success story method')
        print("printing success_story ")
    except Exception:
        print(exception)

class Java_marathon(number_of_courses):
    try:
      def student(self):
        print("java marathon student")
    except Exception:
        print(exception)
j=  number_of_courses()
j.student()

k=Java_marathon()
k.student()
logging.info("In this example 'student' method in class 'number_of_courses' is overridden by 'student' method in 'Java_marathon' class")


#2
class FSDS:
    try:
       logging.info('Student method')
       def student(self):
         print("1000 students enrolled in 2021")
       logging.info('Success story method')
       def success_story(self):
        print("xxx students succeeded ")
    except Exception:
        print(exception)

class Mysql(FSDS):
    try:
      def student(self):
        print("500 students enrolled")
    except Exception:
        print(exception)
j=  FSDS()
j.student()
k=Mysql()
k.student()

#3
logging.info('Internship class')
class Internship:
    logging.info('method creation inside Internship class')
    try:
     def __init__(self):
        self.__certificate='100 students got certified'
     def students(self):
        print(self.__certificate)
    except Exception as e:
        print(e)
class ML_internship(Internship):
    logging.info('method creation inside ML internship class')
    try:
     def __init__(self):
        self.__certificate='10 students got certified'
     def students(self):
        print(self.__certificate)
    except Exception as e:
        print(e)

object1=Internship()
object1.students()
object2=ML_internship()
object2.students()

logging.warning('Overriding examples completed')


#Polymorphism
#1
logging.info('Polymorphism in OOPS')
class ineuron_regular_student:
    def ML_DL(self):
        try:
          print('This is  ML_DL live course student')
        except Execption as e:
            print(e)
class Internship_student:
    def ML_DL(self):
        try:
          print('This is ML_DL Internship student')
        except:
            pass
def polymorphism(k):
    k.ML_DL()
m=ineuron_regular_student()
n=Internship_student()
polymorphism(m)
polymorphism(n)


#2
class _1:
    def ML_DL(self):
        try:
          print('This is  ML_DL student from batch-1')
        except Execption as e:
            print(e)
class _2:
    def ML_DL(self):
        try:
          print('This is ML_DL student from batch-2')
        except:
            pass
        finally:
            print('Finally found the Polymorphism of OOPS!!!')
def polymorphism(k):
    k.ML_DL()
m=_1()
n=_2()
polymorphism(m)
polymorphism(n)

#3
class ineuron:
    def Lokesh(self):
        try:
          print('Lokesh is a student')
        except Execption as e:
            print(e)
class office:
    def Lokesh(self):
        try:
          print('Lokesh is a employee')
        except:
            pass
        finally:
            print('This is allotrophic nature of Lokesh')
def polymorphism(k):
    k.Lokesh()
m=ineuron()
n=office()
polymorphism(m)
polymorphism(n)