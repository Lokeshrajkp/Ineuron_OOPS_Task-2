import logging
logging.basicConfig(filename='abs.log',level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
logging.info('abstraction in oops')

#1
class jobs:
    logging.info('method creation in jobs class')
    try:
       logging.info('hiding job_guarantee in class')
       __jobguarantee= "FSDS"
       def students(self):
        print(self.__jobguarantee)
    except BaseException:
        pass
    finally:
       print('Abstraction example')
i = jobs()
i.students()
logging.warning('example 1 completed')


#2
class ineuron:
    try:
       logging.info('method creation in ineuron class')
       __student_contact_details='file.data'
       def students(self):
         print(self.__student_contact_details)
    except BaseException:
        pass
    finally:
       print('Student contact fetching completed')
i = ineuron()
i.students()
logging.warning('example 2 completed')


#3
class company:
    try:
       logging.info('method creation in company class')
       __blog='blogs data'
       def students(self):
        print(self.__blog)
    except BaseException:
        pass
    finally:
       print('Students blogs')
i = company()
i.students()
logging.warning('example 3 completed')


#4
class Sudhanshu_class:
    try:
       logging.info('method creation in  Sudhanshu_class')
       __feedback='Good'
       def student(self):
        print(Sudhanshu_class.__feedback)
    except BaseException:
        pass
    finally:
       print('Overall rating is good')
i = Sudhanshu_class()
i.student()
logging.warning('example 3 completed')


#5
class num_course:
    try:
       logging.info('method creation in num_course class')
       __count=10
       def Java(self):
        print(num_course.__count)
    except BaseException:
        pass
    finally:
       print('success')
i = num_course()
i.Java()
logging.warning('example 4 completed')

#6
class affiliates:
    try:
       logging.info('method creation in affiliate class')
       __get_rewards=1000
       def DL(self):
        print(affiliates.__get_rewards)
    except BaseException:
        pass
    finally:
       print('reward guaranted')
i = affiliates()
i.DL()
logging.warning('example 5 completed')