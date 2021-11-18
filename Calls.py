class Calls:

    def __init__(self, timing, src, dest):
        self.timing = float(timing)
        self.src = int(src)
        self.dest = int(dest)
        self.num_of_elev = 0  # default
        if (self.dest - self.src) > 0:
            self.type = 1  # UP
        if (self.dest - self.src) < 0:
            self.type = -1  # DOWN

    def assign_elevator(self, num):
        self.num_of_elev = num

    # def allocatedTo(self):
    #   """This methods return the index of the Elevator in the building to which this call
    #   was assigned to, if not yet Assigned --> return -1"""
    # if self._assignedEle == None:
    #    return -1
    # return self._assignedEle
#       #  return self._assignedEle
