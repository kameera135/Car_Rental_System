class Invoice:
    def __init__(self, reservation, daily_rate):
        self.reservation = reservation
        self.daily_rate = daily_rate
        self.total_days = (reservation.end_date - reservation.start_date).days + 1
        self.total_amount = self.daily_rate * self.total_days

    def generate_invoice(self):
        return (f"\nINVOICE:\n\tCustomer: {self.reservation.customer.name}\n"
                f"\tVehicle: {self.reservation.vehicle.display_info()}\n"
                f"\tDuration: {self.total_days} days\n"
                f"\tDaily Rate: ${self.daily_rate:.2f}\n"
                f"\tTotal Amount: ${self.total_amount:.2f}")
