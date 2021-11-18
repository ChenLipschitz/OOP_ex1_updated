import json
import csv
import Offline
from Calls import Calls
from Building import Building
from Offline import Offline


def main(file_name, csv_name):
    def load_json_file(file_name):
        try:
            with open(file_name, "r") as file:
                config = json.load(file)
                build = Building(config["_minFloor"], config["_maxFloor"], config["_elevators"])
                print(3)
                return build
        except IOError as e:
            print(e)

    def load_csv_file(csv_name):
        try:
            with open(csv_name) as csv_file:
                calls_reader = csv.reader(csv_file)
                elv_list = list()
                for line in calls_reader:
                    call = Calls(line[1],line[2], line[3])
                    Offline.allocated(call, elv_list)

            extract_back_to_csv(elv_list, csv_name)
        except IOError as e:
            print(e)

    def extract_back_to_csv(calls_list, name):
        f = open(name, "w")  # name of assigned calls csv
        for y in range(0, len(calls_list) - 1):
            str_c = str(calls_list[y])
            f.write(str_c + "\n")
        str_c = str(calls_list[len(calls_list) - 1])  # last line without \n
        f.write(str_c)
        f.close()

    load_json_file(file_name)
    load_csv_file(csv_name)
