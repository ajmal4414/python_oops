class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

    def seating_capacity(self,capacity):
        return f"The seating capacity of a {self.name}is{capacity} passengers"
    def fare(self,capacity):
        fare=capacity*100
        return fare

class bus(vehicle):

    def fare(self):
        fr=vehicle.fare(self,50)
        charge=fr+((fr*10)/100)
        print('total fare is',charge)

B=bus('sss',110,10)
B.fare()
