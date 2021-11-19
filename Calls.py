import Elevator

class Calls:
    INIT = 0
    GOING2SRC = 1
    GOIND2DEST = 2
    DONE = 3
    UP = 1
    DOWN = -1

    def __init__(self, _callTime, _src, _dest):
        self._callTime = _callTime
        self.src = _src
        self.dest = _dest
        self._assignedEle = -1


    def get_call_time(self):
        return self._callTime
    def getSrc(self):
        return (int)(self.src)

    def getDest(self):
        return (int)(self.dest)

    def getType(self):
        if self.src > self.dest:
            return self.DOWN
        return self.UP

    def setElevator(self, index):
        self._assignedEle = index

    def allocatedTo(self):
        if self._assignedEle == None:
            return -1
        return self._assignedEle

    def __str__(self):
        return f"the time of call: {self._callTime} \t source floor: {self.src} \t destination floor: {self.dest} \n\t" \
               f"the elevator of the call: {self._assignedEle}"
