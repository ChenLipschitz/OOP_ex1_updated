
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
        minTime = float("inf")
        for elev in self._building.elevators_list:
            optTime = self.timeForService(elev, call)
            if optTime < minTime:
                minTime = optTime
                optElev = elev
        numElev = optElev.id
        call.setElevator(numElev)
        optElev.UpdateListOfCalls(call)

    def timeForService(self, elev, call):
        def total_distance_floors(elev):
            total = 0
            for cl in elev.call_list:
                total = total + abs(cl.dest - cl.src)
            return total

        def calcTotal():
            num_of_calls = len(elev.call_list)
            sum_distance = total_distance_floors(elev)
            total_open_close = (num_of_calls * (elev.open_time + elev.close_time))
            total_start_stop = (num_of_calls * (elev.start_time + elev.stop_time))
            ride_time = math.ceil(sum_distance * elev.time_per_floor)
            temp_time = total_start_stop + total_open_close + ride_time
            return temp_time

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
                temp_time = calcTotal()
            return temp_time

        if elev.getState() == -1:
            if elev.maxFloor < call.src and elev.minFloor > call.dest:
                temp_time = float("inf")
            else:
                temp_time = calcTotal()
            return temp_time

        else:
            return float("inf")

    def updateEntries(self, file_name="Ex1_Calls"):
        cl_list = []
        if len(self._building._elevators_list) == 0:
            Preprocessing.saveToCsv(file_name, self.cl_list)
            return 1
        elif len(self._building._elevators_list) == 1:
            for call in self.cl_list:
                call[5] = 0
            Preprocessing.saveToCsv(file_name, self.cl_list)
            return 1
        for call in self.cl_list:
            call_obj = Calls(_callTime=call[1], _src=call[2], _dest=call[3])
            cl_list.append(call_obj)
            self.assignElevators(call_obj)
        ELEVATOR_INDEX = 0
        for call in self.cl_list:
            call[5] = Calls.allocatedTo( cl_list[ELEVATOR_INDEX])
            ELEVATOR_INDEX += 1
        Preprocessing.saveToCsv(file_name, self.cl_list)
        return 1



