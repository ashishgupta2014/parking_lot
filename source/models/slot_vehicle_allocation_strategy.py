from source.utils.constant_enums import VehicleTypes


class AbstractVehicleAllocation:
    """Abstract class"""

    @classmethod
    def allocate(cls, slot: int):
        """allocation logic"""


class AllocateVehicleTypeOnSlot(AbstractVehicleAllocation):
    """Strategy to allocate vehicle on specific slot"""

    @classmethod
    def allocate(cls, slot: int):
        """Allocation Algorithm"""
        # Assuming 1 slot for the Truck
        # Next 2 slot for the Bike
        # other slots for any type of car
        if slot == 1:
            return VehicleTypes.TRUCK.name
        elif slot in [2, 3]:
            return VehicleTypes.BIKE.name
        else:
            return VehicleTypes.CAR.name