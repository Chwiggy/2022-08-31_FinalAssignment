import pandas as pd
import geopandas as gp
import folium

def convert_to_csv(file_path):
    dataframe = pd.read_csv(file_path)
    dataframe.to_csv("stops.csv")
    return dataframe

def convert_stop_locations(dataframe):
    #converting pd.DataFram to gp.GeoDataFrame, and setting the Coordinate Reference System to WGS 84
    stops_gdf = gp.GeoDataFrame(dataframe, geometry=gp.points_from_xy(dataframe.stop_lon, dataframe.stop_lat)).set_crs(epsg=4326, inplace=True)
    return stops_gdf

def find_centre_rough(geodataframe):
    center_lon_lat = geodataframe.dissolve().centroid
    return center_lon_lat

def convert_for_folium(point_lon_lat):
    #returns a list of format longitude latitude from Geopandas Geometry Object
    shapely_point = point_lon_lat[0]
    coordinates_list = shapely_point.coords[:]
    point_tuple = coordinates_list[0]
    point_lat = point_tuple[0]
    point_lon = point_tuple[1]
    location = [point_lon, point_lat]
    return location

def embed_map(m, title):
    from IPython.display import IFrame
    m.save(f'{title}.html')
    return IFrame(f'[{title}.html', width='100%', height='750px')

def main():
    stops_gdf = convert_stop_locations(convert_to_csv("2022-07-26_RNV_GTFS_Schedule\\stops.txt"))
    print(stops_gdf.head())

    #exporting a shp-file for use in a Desktop GIS environment
    stops_gdf.to_file("stops.shp")

    #exporting an html file with our stop locations
    center_for_folium = convert_for_folium(find_centre_rough(stops_gdf))
    map = folium.Map(location = center_for_folium, tiles='OpenStreetMap' , zoom_start = 11)
    embed_map(stops_gdf.explore("platform_code", m=map), "stops_map")


if __name__ == "__main__":
    main()
    