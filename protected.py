#protected accessmethod
# class Student:
# protectrd data members
#     _name=None
#     _roll=None
#     _branch=None

    # def __init__(self,name,roll,branch):
    #     self._name=name
    #     self._roll=roll
    #     self._branch=branch

#protected member function
    # def displayrollandbranch(self):
    #     print('name:',self._name)
    #
    #     print("Roll:",self._roll)
    #     print("branch:",self._branch)

#derived class
# obj=Student("TOM",6767,"PYTHON")
# obj.displayrollandbranch()

# public acess method
class student:
#protectrd data members
    _name=None
    _roll=None
    _branch=None

    def __init__(self,name,roll,branch):
      self._name = name
      self._roll=roll
      self._branch=branch

      print("name:",self._name)
      print("roll:",self._roll)
      print("branch:",self._branch)


class myclass(student):

    def __init__(self,name,roll,branch):
        student.__init__(self,name,roll,branch)


    def displaydetails(self):

        print("name",self._name)

        self.displaydetails()

obj = myclass("vishnu",4544,"python")



a=myclass("tom",6676,"stack")