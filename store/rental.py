class RentalStore:
    def __init__(self):
        self.vehicles = []

    #Only for vehicle preload
    def preload_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    #Add vehicle to admin
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Added vehicle: {vehicle.display_info()}")
        
    
    #Remove vehicle from list
    def remove_vehicle(self, registration_number):
        for v in self.vehicles:
            if v.registration_number == registration_number:
                self.vehicles.remove(v)
                print(f"Removed vehicle: {v.display_info()}")
                return
        print("Vehicle not found.")


    #Find vehicles from register number
    def find_vehicle(self, registration_number):
        for v in self.vehicles:
            if v.registration_number == registration_number:
                return v
        return None
    
    #Display all vehicles
    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicles in store.")
        else:
            print("\nAvailable Vehicles:")
            for v in self.vehicles:
                status = "Available" if v.is_available() else "Rented"
                print(f"\t{v.display_info()} - {status}")
