class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

    def seating_capacity(self,capacity):

        return f"The seating capacity of a {self.name} is {capacity} passengers"


class bus(vehicle):
    def seating_capacity(self,capacity):
        return f"the seating capacity of a {self.name} is {capacity} passengers"

B=bus('bus',110,50)
print(B.seating_capacity(50))