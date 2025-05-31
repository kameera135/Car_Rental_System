from vehicle.van import Van
from vehicle.truck import Truck
from vehicle.suv import SUV
from vehicle.sedan import Sedan
from vehicle.sportsCar import SportsCar

def preload_vehicles(store):
    # Vans
    store.preload_vehicle(Van("Toyota", "HiAce", 2021, "REG-001", 8, has_sliding_doors=True))
    store.preload_vehicle(Van("Ford", "Transit", 2022, "REG-002", 9, has_sliding_doors=False))
    store.preload_vehicle(Van("Nissan", "NV200", 2023, "REG-003", 7, has_sliding_doors=True))

    # Trucks
    store.preload_vehicle(Truck("Volvo", "FH16", 2021, "REG-101", 2))
    store.preload_vehicle(Truck("Scania", "R500", 2022, "REG-102", 2))
    store.preload_vehicle(Truck("Mercedes", "Actros", 2023, "REG-103", 2))

    # SUVs
    store.preload_vehicle(SUV("Toyota", "Land Cruiser", 2021, "REG-201", 7))
    store.preload_vehicle(SUV("Ford", "Explorer", 2022, "REG-202", 6))
    store.preload_vehicle(SUV("Honda", "CR-V", 2023, "REG-203", 5))

    # Sedans
    store.preload_vehicle(Sedan("Honda", "Civic", 2021, "REG-301", 5))
    store.preload_vehicle(Sedan("Toyota", "Corolla", 2022, "REG-302", 5))
    store.preload_vehicle(Sedan("Mazda", "3", 2023, "REG-303", 5))

    # Sports Cars
    store.preload_vehicle(SportsCar("Porsche", "911", 2021, "REG-401", 2))
    store.preload_vehicle(SportsCar("Ferrari", "F8", 2022, "REG-402", 2))
    store.preload_vehicle(SportsCar("Lamborghini", "Huracan", 2023, "REG-403", 2))
