from customer.customer import Customer

class Admin(Customer):
    def __init__(self, name, customer_id, store):
        super().__init__(name, customer_id)
        self.store = store

    def add_vehicle_to_store(self, vehicle):
        self.store.add_vehicle(vehicle)

    def remove_vehicle_from_store(self, registration_number):
        self.store.remove_vehicle(registration_number)

    def view_all_vehicles(self):
        self.store.display_vehicles()
