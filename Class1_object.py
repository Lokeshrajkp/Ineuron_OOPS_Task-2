#1
import logging
logging.basicConfig(filename='class1.log',level=logging.INFO,format='%(asctime)s %(levelname)s %(name)s %(message)s')
class ineuron_student:
    def FSDS_student(self):
        try:
            logging.info('Started student method creation inside class ineuron_student')
            print('This is FSDS student method')
        except Exception:
           print('logging.exception')
try:
    i=ineuron_student()
    i.FSDS_student()
except Exception:
    print('logging.exception')
logging.info('class ineuron_student is successfully accomplished')
#2
logging.info('Empty class creation example')
try:
    class class1:
        pass
    c=class1()
    print(c)


    class class_type:
       class1='java'

    t=class_type()
    print(t)
except Exception:
      print('logging.exception')
#3
class no_of_courses:
    logging.info('no_of_course class method declaration')
    try:
        def course1(self):
           '''FSDS mehtod'''
           print('FSDS')
        def course2(self):
           '''MLDL mehtod'''
           print('MLDL')
        def course3(self):
           ''' Course3 mehtod'''
           print('DLCLNLP')
    except Exception:
        print('logging.exception')
try:
  c=no_of_courses()
  c.course1()
  c.course2()
  c.course3()
except Exception:
   print('logging.exception')
#4
class blog:
    def business_analytics1(self):
        print('This is BA blog')
    def Bigdata(self):
        print('Big data blog')
    def cyber_security(self):
        print('This is cyber security blog')

b=blog()
b.business_analytics1()
b.Bigdata()
b.cyber_security()

#5
class internship:
    logging.info('internship class method declaration')
    def CV(self):
        try:
          print('Internship in CV')
        except exception as e:
            print(e)

    def Bigdata(self):
        try:
            print('Big data Intership')
        except exception as e:
            print(e)
    def webdevelopment(self):
        try:
           print('This is web development intership portal')
        except exception as e:
            print(e)
try:
    n=internship()
    n.CV()
    n.Bigdata()
    n.webdevelopment()
except exception as e:
    print(e)
#6
logging.info('Job1 class creation')
try:
   class job1:
      def company_secretary(self):
        print('Company Secretary’s core duties include optimising workflow procedures in the office')
   class job2:
     def BDE(self):
        print('An ideal candidate for this job role is a person who is fluent in communication with English')
   class job3:
     def NodeJS_developer(self):
        print('Developing and maintaining all integration of user-facing elements developed by front end developers with server-side logic')

   j1=job1()
   j1.company_secretary()
   j2=job2()
   j2.BDE()
   j3=job3()
   j3.NodeJS_developer()
except Exeption:
    print('Exception')
logging.info('7 examples for class is completd')