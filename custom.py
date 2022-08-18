import pandas as pd
import geopandas as gp

def convert_to_csv(file_path):
    dataframe = pd.read_csv(file_path)
    dataframe.to_csv("stops.csv")
    return dataframe

def convert_stop_locations(dataframe):
    #converting pd.DataFram to gp.GeoDataFrame, and setting the Coordinate Reference System to WGS 84
    stops_gdf = gp.GeoDataFrame(dataframe, geometry=gp.points_from_xy(dataframe.stop_lon, dataframe.stop_lat)).set_crs(epsg=4326, inplace=True)
    return stops_gdf

def main():
    stops_gdf = convert_stop_locations(convert_to_csv("2022-07-26_RNV_GTFS_Schedule\\stops.txt"))
    stops_gdf.head()

    #exporting a shp-file for use in a Desktop GIS environment
    stops_gdf.to_file("stops.shp")

if __name__ == "__main__":
    main()
    