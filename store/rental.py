class RentalStore:
    def __init__(self):
        self.vehicles = []

    def preload_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Added vehicle: {vehicle.display_info()}")

    def remove_vehicle(self, registration_number):
        for v in self.vehicles:
            if v.registration_number == registration_number:
                self.vehicles.remove(v)
                print(f"Removed vehicle: {v.display_info()}")
                return
        print("Vehicle not found.")

    def find_vehicle(self, registration_number):
        for v in self.vehicles:
            if v.registration_number == registration_number:
                return v
        return None

    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicles in store.")
        else:
            print("\nAvailable Vehicles:")
            for v in self.vehicles:
                status = "Available" if v.is_available() else "Rented"
                print(f"\t{v.display_info()} - {status}")
