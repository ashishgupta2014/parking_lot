import os
import sys
from pathlib import Path

from source.parking_lot import ParkingLot

BASE_DIR = Path(__file__).resolve().parent.parent

def main():
    """Command line startup"""
    input_path = os.path.join(BASE_DIR, 'input_1.txt')
    lines = open(input_path, 'r').readlines()
    parking_lot = None
    for line in lines:
        inputs = line.split(' ')
        command = inputs[0].strip()
        if command == 'create_parking_lot':
            parking_lot = ParkingLot.create(pkl_id_prefix=inputs[1].strip(),
                                            floors=int(inputs[2].strip()),
                                            slots=int(inputs[3].strip()))
        elif parking_lot and command == 'display':
            print(parking_lot.display(view_type=inputs[1].strip(), vehicle_type=inputs[2].strip()))
        elif parking_lot and command == 'park_vehicle':
            print(parking_lot.park_vehicle(vehicle_type=inputs[1].strip(),
                                           reg_no=inputs[2].strip(),
                                           color=inputs[3].strip()))
        elif parking_lot and command == 'unpark_vehicle':
            print(parking_lot.un_park_vehicle(slot_id=inputs[1].strip()))
        elif command == 'exit':
            sys.exit(0)


if __name__ == "__main__":
    main()
"""
https://github.com/nikuamit/ParkingLot/blob/master/solution/parking_lot.py
https://github.com/apoorva-dave/ParkingLot/blob/master/ParkingLot.py
"""