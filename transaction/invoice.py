class Invoice:
    def __init__(self, reservation, daily_rate):
        self.reservation = reservation
        self.daily_rate = daily_rate
        self.total_days = (reservation.end_date - reservation.start_date).days + 1
        self.total_amount = self.daily_rate * self.total_days

    def generate_invoice(self):
        return (f"INVOICE:\nCustomer: {self.reservation.customer.name}\n"
                f"Vehicle: {self.reservation.vehicle.display_info()}\n"
                f"Duration: {self.total_days} days\n"
                f"Daily Rate: ${self.daily_rate:.2f}\n"
                f"Total Amount: ${self.total_amount:.2f}")
