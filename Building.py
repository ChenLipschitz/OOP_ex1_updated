import Elevator


class Building:

    def __init__(self, min_floor: int, max_floor: int, elevators: list):
        self.min_floor_building = min_floor
        self.max_floor_building = max_floor
        self.elevators = elevators
