import uuid
from datetime import date

class Payment:
    def __init__(self,customer, invoice, payment_method):
        self.payment_id = str(uuid.uuid4())
        self.customer = customer
        self.invoice = invoice
        self.payment_method = payment_method
        self.payment_date = date.today()
        self.status = "Pending"
        self.discount = 0.0

    def process_payment(self):
        # Simulate successful payment
        self.status = "Paid"
        print(f"Payment of ${self.invoice.total_amount:.2f} received via {self.payment_method}.")

    #Display payment data discounts 
    def display(self):
        return (
            f"\tPayment ID: {self.payment_id}\n"
            f"\tDate: {self.payment_date}\n"
            f"\tStatus: {self.status}\n"
            f"\tAmount Paid: ${self.invoice.total_amount:.2f}\n"
            f"\tDiscount Applied: ${self.discount:.2f}\n"
            f"\tMethod: {self.payment_method}"
        )
