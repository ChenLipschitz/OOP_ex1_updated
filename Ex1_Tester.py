from main import main


if __name__ == "__main__":
    #building 1 with calls a
    algo = main("B1.json", "Calls_a.csv")

    print (algo)

    algo.extract_back_to_csv("Ex1_calls_case_a_1.csv")

