from source.utils.constant_enums import VehicleTypes


class Vehicle:
    """Abstract base Vehicle"""

    def __init__(self, reg_no: str, color: str, vehicle_type: str):
        self.reg_no = reg_no
        self.color: color
        self.vehicle_type = vehicle_type

    def get_reg_no(self):
        """reg_no of vehicle"""
        return self.reg_no

    def get_vehicle_type(self):
        """vehicle type"""
        return self.vehicle_type


class Car(Vehicle):
    """Car vehicle"""
    def __init__(self, reg_no: str, color: str):
        Vehicle.__init__(self, reg_no=reg_no, color=color, vehicle_type=VehicleTypes.CAR.name)


class Bike(Vehicle):
    """Car vehicle"""
    def __init__(self, reg_no: str, color: str):
        Vehicle.__init__(self, reg_no=reg_no, color=color, vehicle_type=VehicleTypes.BIKE.name)


class Truck(Vehicle):
    """Car vehicle"""
    def __init__(self, reg_no: str, color: str):
        Vehicle.__init__(self, reg_no=reg_no, color=color, vehicle_type=VehicleTypes.TRUCK.name)

