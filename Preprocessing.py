import pandas as pd


def saveToCsv(file_name, callsArray):
    df = pd.DataFrame(callsArray)
    df.to_csv(str(file_name), index=False)
    #print(df)


def readCsv(file_name):
    df = pd.read_csv(file_name)
    rows = []
    for index, row in df.iterrows():
        rows.append(list(row))
    return rows


def ReadJson(file_name):
    building_df = pd.read_json(file_name)
    return building_df
