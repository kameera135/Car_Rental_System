from vehicle.car import Car

class SportsCar(Car):
    def __init__(self, make, model, year, registration_number, seats, availability=True):
        super().__init__(make, model, year, registration_number, seats, availability)
