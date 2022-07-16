#1
import logging
logging.basicConfig(filename='cons1.log',level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
class courses:
    try:
      def __init__(self,Datascience,programming,cloud):
        self.Datascience=Datascience
        self.programming=programming
        self.cloud=cloud
      def marketing(self):
        print('Marketing of various courses to increase the business and education')
    except Exception as error:
        pass
c=courses('Datascience','programming','cloud')
print(c)
c.marketing()
logging.info('1st example for class is  finished')
#2
class cloud:
    try:
      def __init__(self):
        pass
      def AWS_cloud_master(self):
        print('AWS is one of the major cloud providers across the globe comes with a variety of services in different tech stacks')
    except Exception:
        print('exception ')
cs=cloud()
print(cs)
cs.AWS_cloud_master()
logging.info('2nd example for class is  finished')

#3
logging.info('Career class')
class career:
 try:
    def exp(self, current_year , start_year):
        return current_year - start_year

    def salary(self,current_salary):
        print("salary" ,current_salary)

    def input_name(self):
        name = input("name")
        return name
 except Exception:
     pass
 finally:
     logging.info('codes for constructor creation in oops is completed')
obj1= career()
print(obj1.input_name())
obj1.salary(10000)
print(obj1.exp(2011,1999))
logging.info('3rd example for class is  finished')
#4
import logging
logging.basicConfig(filename='cons1.log',level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
class courses:
    try:
      def __init__(self,ineuron,oneneuron):
        self.ineuron=ineuron
        self.oneneuron=oneneuron
      def marketing(self):
          print(self.ineuron)
    except Exception as error:
        print(error)
c=courses('Datascience','programming')
print(c)
c.marketing()
logging.info('4th example for class is  finished')


#5
import loggings
logging.basicConfig(filename='cons1.log',level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
class courses:
    company= 'ineuron'
    try:
      def __init__(self):
        pass
      def affiliates(self):
          print(self.company)
    except Exception as error:
        print(error)
c=courses()
print(c)
c.affiliates()
logging.info('5th example for class is  finished')

