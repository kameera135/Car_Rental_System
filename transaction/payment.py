class Payment:
    def __init__(self, invoice, payment_method):
        self.invoice = invoice
        self.payment_method = payment_method
        self.status = "Pending"

    def process_payment(self):
        # Simulate successful payment
        self.status = "Paid"
        print(f"Payment of ${self.invoice.total_amount:.2f} received via {self.payment_method}.")

    def display(self):
        return (f"Payment Status: {self.status}\n"
                f"Amount: ${self.invoice.total_amount:.2f}\n"
                f"Method: {self.payment_method}")
