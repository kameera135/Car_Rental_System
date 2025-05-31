class MaintenanceRecord:
    def __init__(self, vehicle, description, date):
        self.vehicle = vehicle
        self.description = description
        self.date = date

    #Display maintenance record
    def display(self):
        return f"{self.vehicle.display_info()} - Maintenance: {self.description} on {self.date}"
