from customer.customer import Customer

class Admin(Customer):
    def __init__(self, name, customer_id, store):
        super().__init__(name, customer_id)
        self.store = store
        self.customer_list = []

    def add_vehicle_to_store(self, vehicle):
        self.store.add_vehicle(vehicle)

    def remove_vehicle_from_store(self, registration_number):
        self.store.remove_vehicle(registration_number)

    def view_all_vehicles(self):
        self.store.display_vehicles()

    def add_customer(self,customer):
        self.customer_list.append(customer)

    def generate_report(self):
        print("\n📋 CUSTOMER REPORT")
        if not self.customer_list:
            print("No customers found.")
            return

        report_lines = ["CUSTOMER REPORT\n=================\n"]

        #Add line by line details
        for customer in self.customer_list:
            report_lines.append(f"Customer: {customer.name} (ID: {customer.customer_id})")

            if customer.rented_vehicles:
                report_lines.append("Rented Vehicles:")
                for v in customer.rented_vehicles:
                    report_lines.append(f" - {v.display_info()}")
            else:
                report_lines.append("No vehicles currently rented.")

            if hasattr(customer, 'reward_points'):
                report_lines.append(f"Reward Points: {customer.reward_points}")

            report_lines.append("")  # newline

        report_text = "\n".join(report_lines)

        # Print to console
        print(report_text)

        # Save to file
        with open("customer_report.txt", "w") as file:
            file.write(report_text)

        print("Report saved to 'customer_report.txt'")

