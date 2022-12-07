from source.models.slot_vehicle_allocation_strategy import AbstractVehicleAllocation


class FloorSlot:
    """Define floors in parking lot with slots. Consider each slot can park 1 vehicle type"""

    def __init__(self, floor: int, slot: int, prefix: str, allocated_vehicle_type: AbstractVehicleAllocation):
        self.floor = floor
        self.slot = slot
        self.allocated_vehicle_type = allocated_vehicle_type.allocate(slot=slot)
        self.slot_id = f'{prefix}_{floor}_{slot}'
        self.vehicle = None

    def is_occupied(self) -> bool:
        """slot is occupied or not"""
        return self.vehicle is not None

    def is_vehicle_type_parking_possible(self, vehicle_type_name: str) -> bool:
        """validate parking possible"""
        return self.allocated_vehicle_type == vehicle_type_name

    def park(self, vehicle):
        """park vehicle at slot"""
        self.vehicle = vehicle


    def get_slot_id(self):
        """slot id"""
        return self.slot_id

    def un_park(self):
        """free up slot"""
        self.vehicle = None

    def get_vehicle(self):
        """vehicle on slot"""
        return self.vehicle


