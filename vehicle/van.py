from vehicle.car import Car

class Van(Car):
    def __init__(self, make, model, year, registration_number, seats, has_sliding_doors, availability=True):
        super().__init__(make, model, year, registration_number, seats, availability)
        self.has_sliding_doors = has_sliding_doors
