from Elevator import Elevator
from Building import Building
from Calls import Calls
import math
import Preprocessing

class Offline:
    def __init__(self, buildingfile, callsfile):
        self.building_df = Preprocessing.ReadJson(buildingfile)
        self._building = Building(_minFloor=self.building_df["_minFloor"], _maxFloor=self.building_df["_maxFloor"],
                                  _elevators=self.building_df["_elevators"])
        self.cl_list = Preprocessing.readCsv(callsfile)

    def assignElevators(self, call):
        optElev = None
        minTimeToArrive = float("inf")
        for elev in self._building.elevators_list:
            optTime = self.calcluateTimeToArrive(elev, call)
            if optTime < minTimeToArrive:
                minTimeToArrive = optTime
                optElev = elev
        elevid = optElev.getID()
        call.setElevator(elevid)
        optElev.UpdateListOfCalls(call)

    def calcluateTimeToArrive(self, elev, call):
        def total_distance_floors(elev):
            total = 0
            for cl in elev.call_list:
                total = total + abs(cl.dest - cl.src)
            return total

        if elev.getState() == 0:
            distance = abs(call.dest - call.src)
            sum_start_stop_time = math.ceil(elev.start_time + elev.stop_time)
            sum_open_close_time = math.ceil(elev.open_time + elev.close_time)
            ride = math.ceil(elev.time_per_floor * distance)
            total = sum_open_close_time + sum_start_stop_time + ride
            return total

        if elev.getState() == 1:
            if elev.minFloor > call.src and elev.maxFloor < call.dest:
                temp_time = float("inf")
            else:
                num_of_calls = len(elev.call_list)
                sum_distance = total_distance_floors(elev)
                total_open_close = (num_of_calls * (elev.open_time + elev.close_time))
                total_start_stop = (num_of_calls * (elev.start_time + elev.stop_time))
                ride_time = math.ceil(sum_distance * elev.time_per_floor)
                temp_time = total_start_stop + total_open_close + ride_time
            return temp_time

        if elev.getState() == -1:
            if elev.maxFloor < call.src and elev.minFloor > call.dest:
                temp_time = float("inf")
            else:
                num_of_calls = len(elev.call_list)
                sum_distance = total_distance_floors(elev)
                total_open_close = (num_of_calls * (elev.open_time + elev.close_time))
                total_start_stop = (num_of_calls * (elev.start_time + elev.stop_time))
                ride_time = math.ceil(sum_distance * elev.time_per_floor)
                temp_time = total_start_stop + total_open_close + ride_time
            return temp_time

        else:
            return float("inf")


    def updateEntries(self, file_name):
        ELEVATOR_INDEX = 5
        cl_list = []
        i = 0
        if len(self._building._elevators_list) == 0:
            Preprocessing.saveToCsv(file_name, self.cl_list)
            return 1
        elif len(self._building._elevators_list) == 1:   # if the building has one elevator, allocate this elevator to each call
            for call in self.cl_list:
                call[5] = 0
            Preprocessing.saveToCsv(file_name, self.cl_list)
            return 1
        for call in self.cl_list:
            cl_list.append(Calls(_callTime=call[1], _src=call[2], _dest=call[3]))
            self.assignElevators(Calls(_callTime=call[1], _src=call[2], _dest=call[3]))
            call[ELEVATOR_INDEX] = Calls.allocatedTo(cl_list[i])
            i += 1
        Preprocessing.saveToCsv(file_name, self.cl_list)
        return 1
