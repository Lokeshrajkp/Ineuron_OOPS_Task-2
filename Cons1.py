#1
class courses:
    def __init__(self,Datascience,programming,cloud):
        self.Datascience=Datascience
        self.programming=programming
        self.cloud=cloud
    def marketing(self):
        print('Marketing of various courses to increase the business and education')

c=courses('Datascience','programming','cloud')
print(c)
c.marketing()

#2
class cloud:
    def __init__(self):
        pass
    def AWS_cloud_master(self):
        print('AWS is one of the major cloud providers across the globe comes with a variety of services in different tech stacks')
cs=cloud()
print(cs)
cs.AWS_cloud_master()

#3
class career:

    def exp(self, current_year , start_year):
        return current_year - start_year

    def salary(self,current_salary):
        print("salary" ,current_salary)

    def input_name(self):
        name = input("name")
        return name



obj1= career()
print(obj1.input_name())
obj1.salary(10000)
print(obj1.exp(2011,1999))





