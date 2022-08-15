import pandas as pd


def convert_to_csv(file_path):
    dataframe = pd.read_csv(file_path)
    dataframe.to_csv("stops.csv")

def main():
    convert_to_csv("2022-07-26_RNV_GTFS_Schedule\\stops.txt")
    print("done")

if __name__ == "__main__":
    main()