class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.rented_vehicles = []

    #Rent vehicle
    def rent_vehicle(self, vehicle):
        if vehicle.is_available():
            vehicle.set_availability(False)
            self.rented_vehicles.append(vehicle)
            print(f"{vehicle.display_info()} has been rented.")
        else:
            print("Vehicle is not available for rent.")

    #Vehicle return process
    def return_vehicle(self, registration_number):
        for vehicle in self.rented_vehicles:
            if vehicle.registration_number == registration_number:
                vehicle.set_availability(True)
                self.rented_vehicles.remove(vehicle)
                print(f"{vehicle.display_info()} has been returned.")
                return
        print("No such vehicle found in your rented list.")

    #Display only rented vehicles
    def display_rented_vehicles(self):
        if not self.rented_vehicles:
            print("No vehicles currently rented.")
        else:
            print("Rented Vehicles:")
            for v in self.rented_vehicles:
                print(f"- {v.display_info()}")
