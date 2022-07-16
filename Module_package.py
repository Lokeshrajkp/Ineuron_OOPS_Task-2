import logging
logging.basicConfig(filename='module.log',level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
logging.info('package_module import  in oops')

#1
try:
   logging.info('importing module cons1')
   from Constructor.Cons1 import courses
   obj3=courses('maths','data','Oracle')
   print(obj3)
   print(obj3.Datascience)
   print(obj3.programming)
   print(obj3.cloud)
except ModuleNotFoundError:
    print('Please import valid module')

#2
try:
    logging.info('importing module Encap1_overriding_Polymorphism_')
    from Encap1_overriding_Polymorphism_ import internship
    obj=internship()
    obj.students()
except ModuleNotFoundError:
    print('Please import valid module')



#3
try:
    logging.info('importing _exp method from Career class ')
    from Public1_private_inheritance_abstraction.Career import _exp
    obj = Career()
    print(obj._exp(2021))
except ModuleNotFoundError:
    print('Please import only existing modules')

#4
try:
    logging.info('importing affiliates class from Encap1_overriding_Polymorphism_ module')
    from Encap1_overriding_Polymorphism_ import affiliates
    def new_contact_details(self,new):
        self.__affiliate = new

    object1 = affiliates()
    object1.students()
    object1.__affiliates = '2 Lakh students'
    object1.students_new(' 5 Lakh studens')
    object1.students()
except ModuleNotFoundError:
    print('Please import only existing modules')


#5
try:
    logging.info('')
    from Class1_object import no_of_courses
    print(no_of_courses.course1())
    class course_new :
      def __init__(self,name):
        self._name = name
    obj=course_new('Devops')
    print(obj.name)
except ModuleNotFoundError:
    print('Please import modules which are already present')
logging.info('OOPS tasks-2 is completed')