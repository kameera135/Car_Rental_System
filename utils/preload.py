from ..vahical.van import Van
from ..vahical.truck import Truck
from ..vahical.suv import SUV
from ..vahical.sedarn import Sedan
from ..vahical.sportsCar import SportsCar

def preload_vehicles(store):
    # Vans
    store.add_vehicle(Van("Toyota", "HiAce", 2021, "REG-001", 8, has_sliding_doors=True))
    store.add_vehicle(Van("Ford", "Transit", 2022, "REG-002", 9, has_sliding_doors=False))
    store.add_vehicle(Van("Nissan", "NV200", 2023, "REG-003", 7, has_sliding_doors=True))

    # Trucks
    store.add_vehicle(Truck("Volvo", "FH16", 2021, "REG-101", 2))
    store.add_vehicle(Truck("Scania", "R500", 2022, "REG-102", 2))
    store.add_vehicle(Truck("Mercedes", "Actros", 2023, "REG-103", 2))

    # SUVs
    store.add_vehicle(SUV("Toyota", "Land Cruiser", 2021, "REG-201", 7))
    store.add_vehicle(SUV("Ford", "Explorer", 2022, "REG-202", 6))
    store.add_vehicle(SUV("Honda", "CR-V", 2023, "REG-203", 5))

    # Sedans
    store.add_vehicle(Sedan("Honda", "Civic", 2021, "REG-301", 5))
    store.add_vehicle(Sedan("Toyota", "Corolla", 2022, "REG-302", 5))
    store.add_vehicle(Sedan("Mazda", "3", 2023, "REG-303", 5))

    # Sports Cars
    store.add_vehicle(SportsCar("Porsche", "911", 2021, "REG-401", 2))
    store.add_vehicle(SportsCar("Ferrari", "F8", 2022, "REG-402", 2))
    store.add_vehicle(SportsCar("Lamborghini", "Huracan", 2023, "REG-403", 2))
