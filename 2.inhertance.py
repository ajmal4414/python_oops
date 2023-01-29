class person:
    def speak(self):
        print('i can speak')

class man(person):
    def wear(self):
        print('i wear shirt')

class woman(person):
    def wear(self):
        print(' i wear skirt')

A = man()
A.wear()
A.speak()

B=woman()
B.wear()
B.speak()