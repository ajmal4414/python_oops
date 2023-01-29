"""
inheritance: child class inherit the properties of parent class
"""

class person :
    def __init__(self,name,contactno):
        self.name=name
        self.contactno=contactno

    def address(self):
        print(self.name,self.contactno)

#child class
class Doctor(person):
    pass

class patient(person):
    pass

doc= person('tom',12233)
pat = person('sajin',23343)

doc.address()
pat.address()