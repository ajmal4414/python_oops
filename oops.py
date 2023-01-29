class person:
    def __init__(self,name,age,job):
        self.name=name
        self.age=age
        self.job=job
    def test(self):
        print("hi, my name is" ,self.name,"my age is",self.age,"my job is",self.job)


a=person('john',12,'engineer')
a.test()