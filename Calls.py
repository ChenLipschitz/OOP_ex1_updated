import Elevator

class Calls:


    def __init__(self, _callTime, _src, _dest):
        self._callTime = _callTime
        self.src = _src
        self.dest = _dest
        self._assignedEle = -1

    def getType(self):
        if self.src > self.dest:
            return -1
        return 1

    def setElevator(self, index):
        self._assignedEle = index

    def allocatedTo(self):
        if self._assignedEle == None:
            return -1
        return self._assignedEle

