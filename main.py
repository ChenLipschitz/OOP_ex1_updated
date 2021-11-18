import json
import Building
import csv
import Offline


 # load a json file to the program
from Calls import Calls


def load_json_file(file_name: str):
    try:
        with open(file_name, "r") as file:
            config = json.loads(file)
            build = Building(config["_minFloor"], config["_maxFloor"], config["_elevators"])
            return build
    except IOError as e:
            print(e)

def load_csv_file(csv_name):
    list=[]
    try:
        with open(csv_name) as csv_file:
            calls_reader = csv.reader(csv_file)
            for line in calls_reader:
                call = Calls(line[2],line[3])
                Offline.allocated(call,list)
        extract_back_to_csv(list,csv_name)
    except IOError as e:
            print(e)


def extract_back_to_csv(calls_list, name):
    """ extract CallForElevator list as new csv file, with updated allocated elev column """
    f = open(name, "w")  # name of assigned calls csv
    for y in range(0, len(calls_list) - 1):
        str_c = str(calls_list[y])
        f.write(str_c + "\n")
    str_c = str(calls_list[len(calls_list) - 1])  # last line without \n
    f.write(str_c)
    f.close()
def main():
    if __name__ == "__main__":
        algo = my_algo(r"B2.json", r"Calls_a.csv")
        algo.updateFile("output.csv")







