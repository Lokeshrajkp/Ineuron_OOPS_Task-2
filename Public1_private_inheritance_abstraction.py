#1
import logging
logging.basicConfig(filename='Public.log',level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
class course:
    try:
      logging.info('Public,private,protected methods example1')
      name='FSDS'
      _login_id= "ABCD"
      __password = "zzzz"
      span=12
      def _duration(self ,current_month ):
         return self.span- current_month

      def __duration(self,current_month):
         return self.span - current_month
    except BaseException:
        print('base exception')
obj = course()
print(obj._duration(5))
print(obj._course__duration(6))
print(obj.name)
print(obj._login_id)
print(obj._course__password)

#2
class course:
    try:
      logging.info('Public,private,protected methods example1')
      name = 'FSDS'
      _login_id = "ABCD"
      __password = "zzzz"
      span = 12
      def _duration(self, current_month):
         return self.span - current_month

      def __duration(self, current_month):
         return self.span - current_month
    except BaseException:
        print('exception')

class internship(course):
    try:
        name = 'cyber security'
        _login_id = "cysec"
        __password = "pword"
        span = 8
    except BaseException:
        print('base exception')
ob = internship()
print(ob.name)
print(ob._duration(8))
print(ob._course__duration(9))


#3
class Career:
    try:
      def __init__(self,nodejs,editor,writer):
        self._nodejs=nodejs
        self.__editor=editor
        self.writer=writer
    except BaseException:
        print('base exception')
obj1=Career('akash','sachin','vikas')
print(obj1._nodejs)
print(obj1._Career__editor)
print(obj1.writer)

#4
class Career:
    try:
      _name = "sachin"
      __surname = "vikas"
      YOJ = 2020

      def _exp(self, current_year):
        return current_year - self.YOJ

      def __exp1(self, current_year):
        return current_year - self.YOJ
    except BaseException:
       print('base exception')

obj = Career()
print(obj._exp(2022))
print(obj._Career__exp1(2022))


class employee(Career):
    try:
      _name = "anil"
      __surname = "singh"
      YOJ = 2010
    finally:
        print('finally block execution')
obj2 = employee()
print(obj2._exp(2022))
print(obj2._Career__exp1(2022))
print(obj2)
print(obj2.YOJ)
print(obj2._name)
print(obj2._employee__surname)

#5
class jobs:
    try:
       __jobguarantee= "FSDS"

       def students(self):
         print(self.__jobguarantee)
    except BaseException:
        print('base exception')
i = jobs()
i.students()

#6
class FSDS:
    try:
      name = 'Lokesh'
      _login_id = "ABCD"
      __password = "zzzz"
      span = 12

      def _Certificate(self, current_month):
        return self.span - current_month

      def __Internship(self, current_month):
        return self.span - current_month

    except BaseException:
       print('base exception')

obj = FSDS()
print(obj._Certificate(6))
print(obj._FSDS__Internship(10))
print(obj.name)
print(obj._login_id)
print(obj._FSDS__password)