import pandas as pd
import geopandas as gp

def convert_to_csv(file_path):
    dataframe = pd.read_csv(file_path)
    dataframe.to_csv("stops.csv")
    return dataframe

def convert_stop_locations(dataframe):
    stops_geoframe = gp.GeoDataFrame(dataframe, geometry=gp.points_from_xy(dataframe.stop_lat, dataframe.stop_lon))
    return stops_geoframe

def main():
    stops_geoframe = convert_stop_locations(convert_to_csv("2022-07-26_RNV_GTFS_Schedule\\stops.txt"))
    print(stops_geoframe.head())
    stops_geoframe.to_file("stops.shp")

if __name__ == "__main__":
    main()
    