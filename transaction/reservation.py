class Reservation:
    def __init__(self, customer, vehicle, start_date, end_date):
        self.customer = customer
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date
        self.active = True

    def cancel(self):
        if self.active:
            self.vehicle.set_availability(True)
            self.active = False
            print("Reservation cancelled.")
        else:
            print("Reservation already inactive.")

    def display(self):
        return (f"Reservation: {self.vehicle.display_info()} for "
                f"{self.customer.name} from {self.start_date} to {self.end_date}")
