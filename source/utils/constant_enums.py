from enum import Enum


class VehicleTypes(Enum):
    """Types of supported vehicle"""
    CAR = 'Car'
    BIKE = 'Bike'
    TRUCK = 'Truck'

    @classmethod
    def get_name_mapping(cls, name):
        """map by name"""
        return {ele.name: ele.name for ele in cls}[name]

    @classmethod
    def build_heap_memory(cls, floors_slots):
        """create min heap respect each vehicle type to get next free slot"""
        vehicle_free_slots = dict()
        for ele in cls:
            vehicle_free_slots[ele.name] = []
            for slot in floors_slots:
                if slot.allocated_vehicle_type == ele.name:
                    vehicle_free_slots[ele.name].append(slot)
        return vehicle_free_slots

    @classmethod
    def vehicle_registry(cls, vehicle_type):
        """Register vehicle operational class"""
        from source.models.vehicle import Car, Bike, Truck
        mapping = {cls.CAR.name: Car,
                   cls.BIKE.name: Bike,
                   cls.TRUCK.name: Truck}
        return mapping.get(vehicle_type)



class ViewType(Enum):
    """Parking lot Presentation types"""
    FREE_COUNT = 'free_count'
    FREE_SLOTS = 'free_slots'
    OCCUPIED_SLOTS = 'occupied_slots'
