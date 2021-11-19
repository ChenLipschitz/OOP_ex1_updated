from Elevator import elevator
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

    def allocated(self, call):
        choosenelev = None
        minTimeToArrive = float("inf")
        tmpTime = 10000
        for elev in self._building._elevators_list:
            tmpTime = self._CalcluateTimeToArrive(elev, call)
            if tmpTime < minTimeToArrive:
                minTimeToArrive = tmpTime
                choosenelev = elev
        elevid = choosenelev.getID()
        call.setElevator(elevid)
        choosenelev.UpdateListOfCalls(call)

    def _CalcluateTimeToArrive(self, elev, call):
        def checkIfLegal(elev, call):
            if elev.getState() == -2:  # if error, pass
                return False
            elif elev.getState() != 0:  # not in level mode
                if elev.getState() != call.getType():
                    return False
            elif elev.getState() == 1 and call.getType() == 1:  # UP
                if elev.minFloor > call.src and elev.maxFloor < call.dest:
                    return False
                else:
                    return True
            if elev.getState() == -1 and call.getType() == -1:  # DOWN
                if elev.maxFloor < call.src and elev.minFloor > call.dest:
                    return False
                else:
                    return True

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


    def updateFile(self, file_name="Ex1_Calls") -> None:
        # if the number of elevator is 0 then dont change the file and save it as it is
        if len(self._building._elevators_list) == 0:
            Preprocessing.saveToCsv(file_name, self.cl_list)
            return
        # if the number of elevator is 1 then change the last column of the all the calls to 0,
        # meaning send all the calls to elevator 0 and then save the array of calls to a new fil
        elif len(self._building._elevators_list) == 1:
            for call in self.cl_list:
                call[5] = 0
            Preprocessing.saveToCsv(file_name, self.cl_list)
            return
        cl_list = []
        for call in self.cl_list:
            call_obj = Calls(_callTime=call[1], _src=call[2], _dest=call[3])
            cl_list.append(call_obj)
            self.allocated(call_obj)
        index = 0
        for call in self.cl_list:
            call_obj = cl_list[index]
            call[5] = Calls.allocatedTo(call_obj)
            index += 1
        Preprocessing.saveToCsv(file_name, self.cl_list)
        return
