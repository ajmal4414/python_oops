# create simple calculator using single inheritance
class calculator:

    def add(self):
        print(a+b)


    def div(self):
        print(a/b)

    def mul(self):
        print(a*b)

    def sub(self):
        print(a-b)
a=int(input("enter 1st no:"))
b=int(input("enter the 2nd no:"))

obj=calculator()

choice=1
while choice!=0:
    print("1. ADDITION")
    print("2. DIVISION")
    print("3.MULTIPLICATION")
    print("4. SUBSTRACT")
    choice=int(input('enter your choice'))

    if choice==1:
        print(obj.add())
    elif choice ==2:
        print(obj.div())
    elif choice ==3:
        print(obj.mul())
    elif choice ==4:
        print(obj.sub())
    else:
        print('invalid entry')