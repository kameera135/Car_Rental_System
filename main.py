from store.rental import RentalStore
from customer.admin import Admin
from customer.regular_customer import RegularCustomer
from utils.preload import preload_vehicles
from transaction.reservation import Reservation
from transaction.invoice import Invoice
from transaction.payment import Payment
import datetime

def print_menu_regular():
    print("\nCAR RENTAL MANAGEMENT SYSTEM")
    print("1. View Available Vehicles")
    print("2. Rent a Vehicle")
    print("3. Return a Vehicle")
    print("4. View Rented Vehicles")
    print("5. Exit")

def print_menu_admin():
    print("\nCAR RENTAL MANAGEMENT SYSTEM")
    print("1. View Available Vehicles")
    print("2. Rent a Vehicle")
    print("3. Return a Vehicle")
    print("4. View Rented Vehicles")
    print("5. Add Vehical To Store")
    print("6. Remove Vehical From Store")
    print("7. Exit")

def print_admin_menu():
    print("ADMIN OPTIONS")
    print("6. Add Vehicle")
    print("7. Remove Vehicle")


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

        print_menu_regular()
        if isinstance(user, Admin):
            print_admin_menu()

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

        elif choice == '6' and isinstance(user, Admin):
            # Add Vehicle (admin only)
            category = input("Enter vehicle type (van/truck/suv/sedan/sports): ").lower()
            make = input("Brand: ")
            model = input("Model: ")
            year = int(input("Year: "))
            reg = input("Registration Number: ")
            seats = int(input("Number of Seats: "))

            # import only here to avoid circular issues
            if category == 'van':
                from vehicle.van import Van
                has_doors = input("Has sliding doors (yes/no)? ").lower() == 'yes'
                vehicle = Van(make, model, year, reg, seats, has_doors)
            elif category == 'truck':
                from vehicle.truck import Truck
                vehicle = Truck(make, model, year, reg, seats)
            elif category == 'suv':
                from vehicle.suv import SUV
                vehicle = SUV(make, model, year, reg, seats)
            elif category == 'sedan':
                from vehicle.sedan import Sedan
                vehicle = Sedan(make, model, year, reg, seats)
            elif category == 'sports':
                from vehicle.sportsCar import SportsCar
                vehicle = SportsCar(make, model, year, reg, seats)
            else:
                print("Unknown vehicle type.")
                continue

            user.add_vehicle_to_store(vehicle)

        elif choice == '7' and isinstance(user, Admin):
            reg = input("Enter registration number to remove: ")
            user.remove_vehicle_from_store(reg)

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
