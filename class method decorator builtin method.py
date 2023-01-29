#class method decorator builtin method
class student:
    school_name='abc school'

    def __init__(self,name,age):

        self.name=name
        self.age=age

    def show(self):
        print('student:',self.name,self.age,student.school_name)

    def change_age(self,new_age):
        self.age=new_age

    @classmethod
    def modify_school_name(cls,new_name):
        cls.school_name=new_name

s1=student("tom",16)

s1.show()
s1.change_age(20)

student.modify_school_name("xyz school")
s1.show()

# user defined decorators

# def say(func):
#     def wrapper(*args, **kwargs):
#         func(*args,**kwargs)
#     return wrapper()
# @say
# def greet(name):
#     print("hello ()", format(name))
# greet("tom")