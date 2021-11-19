from Calls import Calls

class elevator():
    UP = 1
    LEVEL = 0
    DOWN = -1
    ERROR = -2

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

    def gettimeForOpen(self):
        return (float)(self.openTime)

    def gettimeForClose(self):
        return (float)(self.closeTime)

    def getState(self):
        if len(self.call_list) == 0:
            return self.LEVEL
        if self.call_list[len(self.call_list) - 1].getType() is Calls.UP:
            return self.UP
        elif self.call_list[len(self.call_list) - 1].getType() is Calls.DOWN:
            return self.DOWN
        return self.LEVEL


    def getStartTime(self):
        return (float)(self.startTime)

    def getStopTime(self):
        return (float)(self.stopTime)

    def __str__(self):
        return f"elevator number {self.id}: \n\t speed = {self.speed} \n\t minFloor = {self.minFloor} \n\t" \
               f"maxFloor = {self.maxFloor} \n\t close time = {self.open_time} \n\t" \
               f"open time = {self.open_time} \n\t start time = {self.start_time} \n\t" \
               f"stop time = {self.stop_time}"
