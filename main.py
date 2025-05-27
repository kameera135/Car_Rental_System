from store.rental import RentalStore
from customer.admin import Admin
from customer.regular_customer import RegularCustomer
from utils.preload import preload_vehicles
from transaction.reservation import Reservation
from transaction.invoice import Invoice
from transaction.payment import Payment
import datetime

def print_menu():
    print("\nCAR RENTAL MANAGEMENT SYSTEM")
    print("1. View Available Vehicles")
    print("2. Rent a Vehicle")
    print("3. Return a Vehicle")
    print("4. View Rented Vehicles")
    print("5. Exit")

def main():
    store = RentalStore()
    preload_vehicles(store)

    print("Welcome to CRMS")
    user_type = input("Are you an Admin (A) or Regular Customer (R)? ").strip().lower()

    name = input("Enter your name: ")
    customer_id = input("Enter your ID: ")

    if user_type == 'a':
        user = Admin(name, customer_id, store)
    else:
        user = RegularCustomer(name, customer_id)

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            store.display_vehicles()

        elif choice == '2':
            reg = input("Enter registration number of the vehicle to rent: ")
            vehicle = store.find_vehicle(reg)

            if vehicle and vehicle.is_available():
                try:
                    start_str = input("Enter start date (YYYY-MM-DD): ")
                    end_str = input("Enter end date (YYYY-MM-DD): ")
                    start_date = datetime.datetime.strptime(start_str, "%Y-%m-%d").date()
                    end_date = datetime.datetime.strptime(end_str, "%Y-%m-%d").date()

                    user.rent_vehicle(vehicle)
                    reservation = Reservation(user, vehicle, start_date, end_date)
                    invoice = Invoice(reservation, daily_rate=100.0)
                    print(invoice.generate_invoice())

                    method = input("Enter payment method (e.g., Credit Card): ")
                    payment = Payment(invoice, method)
                    payment.process_payment()

                except Exception as e:
                    print("Error processing reservation:", e)
            else:
                print("Vehicle not found or unavailable.")

        elif choice == '3':
            reg = input("Enter registration number of the vehicle to return: ")
            user.return_vehicle(reg)

        elif choice == '4':
            user.display_rented_vehicles()

        elif choice == '5':
            print("Thank you for using CRMS!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
