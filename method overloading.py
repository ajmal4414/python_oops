#methodoverloading
# class methodoverloading:
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)

# a=methodoverloading()
# a.add(5,10,5)
# a.add(5,10,5)

#methodoveriding
class class1:
    def display(self):
        print("hello from class1")
class class2:
    def display(self):
        print("hello from class2")

c1=class1()
c2=class2()

c1.display()
c2.display()