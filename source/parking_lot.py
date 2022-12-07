import heapq

from source.utils.constant_enums import VehicleTypes, ViewType
from source.models.floor_slot import FloorSlot
from source.models.slot_vehicle_allocation_strategy import AllocateVehicleTypeOnSlot

GLOBAL_CONSTANT = 1234


class ParkingLot:
    """Parking Lot application"""

    def __init__(self, floors: int, slots: int, pkl_id_prefix: str = None):
        global GLOBAL_CONSTANT
        self._pkl_id_prefix = pkl_id_prefix or f'PR{GLOBAL_CONSTANT}'
        GLOBAL_CONSTANT += 1
        self._floors_slot = [FloorSlot(
            floor=floor,
            slot=slot,
            prefix=self._pkl_id_prefix,
            allocated_vehicle_type=AllocateVehicleTypeOnSlot()
        ) for slot in range(1, slots + 1) for floor in range(1, floors + 1)]

        self._vehicle_minheap_slots = VehicleTypes.build_heap_memory(self._floors_slot)
        self._occupied_area_by_slot_id = dict()
        self._occupied_area_by_reg_no = dict()


    def group_by_vehicle_type_free_slots_count(self, vehicle_type: str):
        """Vehicle type free slots count"""
        display = dict()
        for slot in self._floors_slot:
            if slot.is_vehicle_type_parking_possible(VehicleTypes.get_name_mapping(vehicle_type)) \
                    and not slot.is_occupied():
                display[slot.floor] = display.get(slot.floor, 0) + 1
        return display

    def slots_display(self, vehicle_type: str, is_occupied: bool):
        """occupied/unoccupied display"""
        display = dict()
        for slot in self._floors_slot:
            if slot.floor not in display:
                display[slot.floor] = []
            if slot.is_vehicle_type_parking_possible(VehicleTypes.get_name_mapping(vehicle_type)) \
                    and slot.is_occupied() is is_occupied:
                display[slot.floor].append(slot.slot)
        return display

    @classmethod
    def create(cls, *, pkl_id_prefix: str, floors: int, slots: int):
        """Create Parking Lot"""
        return ParkingLot(pkl_id_prefix=pkl_id_prefix, floors=floors, slots=slots)

    def park_vehicle(self, vehicle_type: str, reg_no: str, color: str):
        """park vehicle to valid floor and slot"""
        free_slots = self._vehicle_minheap_slots[vehicle_type]
        if not free_slots:
            return f'Parking is full for vehicle type {vehicle_type}'
        available_slot = free_slots.pop(0)
        vehicle = VehicleTypes.vehicle_registry(vehicle_type)
        if vehicle:
            self._occupied_area_by_slot_id[available_slot.get_slot_id()] = available_slot
            self._occupied_area_by_reg_no[reg_no] = available_slot
            available_slot.park(vehicle(reg_no, color))
            return f'Vehicle has been parked on id {available_slot.get_slot_id()}'
        return f'Currently Parking not available for vehicle type {vehicle_type}'

    def un_park_vehicle(self, *, reg_no: str = None, slot_id: str = None):
        """free up slot"""
        if reg_no or slot_id:
            try:
                if reg_no:
                    slot = self._occupied_area_by_reg_no[reg_no]
                    vehicle = slot.get_vehicle()
                    slot.un_park()
                    del self._occupied_area_by_slot_id[slot.get_slot_id()]
                    del self._occupied_area_by_reg_no[vehicle.reg_no]
                    self._vehicle_minheap_slots[vehicle.get_vehicle_type()].append(slot)
                    return f'Slot is free {slot.get_slot_id()}'
                elif slot_id:
                    slot = self._occupied_area_by_slot_id[slot_id]
                    vehicle = slot.get_vehicle()
                    slot.un_park()
                    del self._occupied_area_by_slot_id[slot_id]
                    del self._occupied_area_by_reg_no[vehicle.reg_no]
                    self._vehicle_minheap_slots[vehicle.get_vehicle_type()].append(slot)
                    return f'Slot is free {slot_id}'
            except KeyError:
                return f'Invalid Ticket {slot_id or reg_no}'
        return f'Either reg_no/slot_id is needed to free up parking area'

    def display(self, view_type: str, vehicle_type: str):
        """display slots"""
        if view_type == ViewType.FREE_COUNT.value:
            return self.group_by_vehicle_type_free_slots_count(vehicle_type)
        elif view_type == ViewType.FREE_SLOTS.value:
            return self.slots_display(vehicle_type, False)
        elif view_type == ViewType.OCCUPIED_SLOTS.value:
            return self.slots_display(vehicle_type, True)
