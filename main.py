import json
import math
import Offline
import csv

import Calls
import Building
import Elevator
import pandas as pd

    def _init(self, calls_file, building_file):
        calls_file = open(calls_file)


 # load a csv file to the program
    def load_from_file(file_name: str):
     try:
         with open(file_name, "r") as file:
                 config = json.loads(file)
                 build = Building(config["_minFloor"], config["_maxFloor"], config["_elevators"])
                 return build
     except IOError as e:
             print(e)



 def main():# change the folder path to file name
     count = 1
     flag = True
     df = pd.read_csv(r"Calls_a.csv", header = None)
     print(df)
      df['time_dif_next_elv'] = df[1].diff()
      list_time = df['time_dif_next_elv']
      if flag == True:
          time.sleep(df.loc[0][1])
          allocate_elev(df[2][0],df[3][0])
          flag = False
      if flag == False:
          for count in len(df[0]):
              time.sleep(list_time[count])
              currentPosition(df[1].diff()[count])
              allocate_elev(df[2][count],df[3][count])
              count += 1
      print(list_time[1])





if __name__ == "__main__":
    algo = my_algo(r"B2.json", r"Calls_a.csv")
    algo.updateFile("output.csv")

