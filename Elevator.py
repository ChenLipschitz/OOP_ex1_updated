from Calls import Calls

class Elevator:

    def __init__(self, _id, _speed, _minFloor, _maxFloor, _closeTime, _openTime,_startTime, _stopTime):
        self.id = _id
        self.speed = _speed
        self.minFloor = _minFloor
        self.maxFloor = _maxFloor
        self.time_per_floor = 1 / self.speed
        self.close_time = _closeTime
        self.open_time = _openTime
        self.start_time = _startTime
        self.stop_time = _stopTime
        self.call_list = []

    def UpdateListOfCalls(self, call):
        print(self.call_list)
        self.call_list.append(call)

    def getID(self):
        return (int)(self.id)

    def getSpeed(self):
        return (float)(self.speed)

    def getMinFloor(self):
        return (int)(self.minFloor)

    def getMaxFloor(self):
        return (int)(self.maxFloor)



    def getState(self):
        if len(self.call_list) == 0:
            return 0
        if self.call_list[len(self.call_list) - 1].getType()  == 1:
            return 1
        elif self.call_list[len(self.call_list) - 1].getType() == -1:
            return -1
        return 0


    def getStartTime(self):
        return (float)(self.startTime)

    def getStopTime(self):
        return (float)(self.stopTime)

