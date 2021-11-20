import Elevator

class Calls:


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
            return -1
        return 1

    def setElevator(self, index):
        self._assignedEle = index

    def allocatedTo(self):
        if self._assignedEle == None:
            return -1
        return self._assignedEle

    def __str__(self):
        return f"the time of call: {self._callTime} \t source floor: {self.src} \t destination floor: {self.dest} \n\t" \
               f"the elevator of the call: {self._assignedEle}"
