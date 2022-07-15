#1
class course :
     name='FSDS'
     _login_id= "ABCD"
     __password = "zzzz"
     span=12

     def _duration(self ,current_month ):
        return self.span- current_month


     def __duration(self, current_month):
          return self.span - current_month

obj = course()
print(obj._duration(7))
print(obj._course__duration(6))
print(obj.name)
print(obj._login_id)
print(obj._course__password)

#2
class course:
    name = 'FSDS'
    _login_id = "ABCD"
    __password = "zzzz"
    span = 12

    def _duration(self, current_month):
        return self.span - current_month

    def __duration(self, current_month):
        return self.span - current_month

class internship(course):
     name = 'cyber security'
     _login_id = "cysec"
     __password = "pword"
     span = 8

ob = internship()
print(ob.name)
print(ob._duration(8))
print(ob._course__duration(9))


#3
class Career:
    def __init__(self,nodejs,editor,writer):
        self._nodejs=nodejs
        self.__editor=editor
        self.writer=writer
obj1=Career('akash','sachin','vikas')
print(obj1._nodejs)
print(obj1._Career__editor)
print(obj1.writer)

class Career:
    _name = "sachin"
    __surname = "vikas"
    YOJ = 2020

    def _exp(self, current_year):
        return current_year - self.YOJ

    def __exp1(self, current_year):
        return current_year - self.YOJ


obj = Career()
print(obj._exp(2022))
print(obj._Career__exp1(2022))


class employee(Career):
    _name = "anil"
    __surname = "singh"
    YOJ = 2010
obj2 = employee()
print(obj2._exp(2022))
print(obj2._Career__exp1(2022))
print(obj2)
print(obj2.YOJ)
print(obj2._name)
print(obj2._employee__surname)


class jobs:
    __jobguarantee= "FSDS"

    def students(self):
        print(self.__jobguarantee)

i = jobs()
i.students()
