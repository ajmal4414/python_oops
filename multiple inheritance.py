class Emp:
    def empdetails(self):
        print("Employee details")

class Emp1:
    def test(self):
        print('message')

class Emp2(Emp,Emp1):
    def emp2(self):
        print("new employers are welcome")
obj=Emp2()
obj.test()
obj.emp2()