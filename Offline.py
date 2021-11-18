import Building
import math
from Elevator import Elevator
from Building import Building
from Calls import Calls


class Offline:
    def __init__(self, building: Building, cl_list: list):
        self.building = building
        self.cl_list = cl_list

    def allocated(self, call, indexs: list):
        index = 0  # default, num of elevator
        i = 0  # represents the index in the loop
        min_time = 100000000
        if self.contains_level(self.building.elevators):
            # search for the elevator with the shortest arrive time and in level mode
            index = self.level_best_time(self, call)
        else:
            for elev in self.building.elevators:  # if there isn't an elevator in level mode
                if elev.state == -2:  # if error, pass
                    i += 1
                    continue
                if elev.state != 0:  # not in level mode
                    if elev.type is not call.type:  # if the elevator is going up and the call is down-> continue, vice versa
                        i += 1
                        continue
                    if elev.type == 1 and call.type == 1:  # UP
                        if elev.max_floor < call.dest:
                            i += 1
                            continue
                        if elev.min_floor > call.src:
                            i += 1
                            continue
                    if elev.type == -1 and call.type == -1:  # DOWN
                        if elev.max_floor < call.src:
                            i += 1
                            continue
                        if elev.min_floor > call.dest:
                            i += 1
                            continue
                    num_of_calls = len(elev.calls_list)
                    sum_distance = self.total_distance_floors(elev)
                    total_open_close = math.ceil(num_of_calls * (elev.open_time + elev.close_time))
                    total_start_stop = math.ceil(num_of_calls * (elev.start_time + elev.stop_time))
                    ride_time = math.ceil(sum_distance * elev.time_per_floor)
                    temp_time = total_start_stop + total_open_close + ride_time
                    if min_time > temp_time:
                        min_time = temp_time
                        index = i
                i += 1
        elev.calls_list.add(call)
        indexs.append(index)
        return index

    def total_distance_floors(elev: Elevator) -> int:
        total = 0
        for cl in elev.calls_list:
            total = total + abs(cl.dest - cl.src)
        return total

    def contains_level(self) -> bool:
        for el in self.building.elevators:
            if el.state == 0:
                return True
        return False

    def level_best_time(self, call):  # calculates the run time for a level elevator
        i = 0
        min_time = 100000000
        for el in self.building.elevators:
            if el.state == 0:
                temp_time = self.time_level_2_dest(el, call)
                if temp_time < min_time:
                    min_time = temp_time
                    index = i
            i += 1
        return index

    def time_level_2_dest(elev: Elevator, call):
        distance = abs(call.dest - call.src)
        sum_start_stop_time = math.ceil(elev.start_time + elev.stop_time)
        sum_open_close_time = math.ceil(elev.open_time + elev.close_time)
        ride = math.ceil(elev.time_per_floor * distance)
        total = sum_open_close_time + sum_start_stop_time + ride
        return total
