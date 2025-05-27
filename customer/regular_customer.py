from customer.customer import Customer

class RegularCustomer(Customer):
    def __init__(self, name, customer_id):
        super().__init__(name, customer_id)
