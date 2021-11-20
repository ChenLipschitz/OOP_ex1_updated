from Elevator import Elevator
import pandas as pd
import json


class Building:
    def __init__(self, _minFloor, _maxFloor, _elevators):
        self._maxFloor = _maxFloor
        self._minFloor = _minFloor
        self._elevators_list = []
        for item in _elevators:
            self._elevators_list.append(Elevator(_id=item["_id"], _speed=item["_speed"], _minFloor=item["_minFloor"],
                                                 _maxFloor=item["_maxFloor"], _closeTime=item["_closeTime"],
                                                 _openTime=item["_openTime"], _startTime=item["_startTime"],
                                                 _stopTime=item["_stopTime"]))

    @property
    def elevators_list(self):
        return self._elevators_list

