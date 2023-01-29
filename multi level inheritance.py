#multilevel inheritaance
class grandfather:
    def ownhouse(self):
        print('grandfather house')

class Father(grandfather):
    def ownbike(self):
        print('father,s bike')

class son(Father):
    def ownbook(self):
        print('son have a book')

A = son()
A.ownhouse()
A.ownbike()
A.ownbook()



