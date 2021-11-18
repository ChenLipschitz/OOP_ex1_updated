class Elevator:

    def __init__(self, ID, min_floor, max_floor, open_time, close_time, start_time, stop_time, speed):
        self.state = 0
        self.ID = ID
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.open_time = open_time
        self.close_time = close_time
        self.start_time = start_time
        self.stop_time = stop_time
        self.speed = speed
        self.time_per_floor = 1 / self.speed
        self.calls_list = []

    # self.calls_list.append(AllocatedCall.first_call(self))
    # state: leve = 0, up = 1, down = -1, error = -2

    def insert_call(self, call):
        self.calls_list += [call]

    def current_state(self):
        if len(self.calls_list) == 0:
            self.state = 0
        if self.calls_list[0].dest - self.calls_list[0].src > 0:
            self.state = 1
        if self.calls_list[0].dest - self.calls_list[0].sec < 0:
            self.state = -1
