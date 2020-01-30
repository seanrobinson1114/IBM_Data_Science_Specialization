# Imports
import pandas as pd
import folium

# load data into dataframe
crime_rates_df = pd.read_csv(
    "/home/sean/software/coursera/IBM_Data_Science/Data_Visualization_with_Python/final_project/IBM_Data_Science_Specialization/Police_Department_Incidents_-_Previous_Year__2016_.csv"
)
print(crime_rates_df)

# initialize data
data = [['CENTRAL',17666],['NORTHERN',20100],['PARK',8699],['SOUTHERN',28445],['MISSION',19503],['TENDERLOIN',9942],['RICHMOND',8922],['TARAVAL',11325],['INGLESIDE',11594],['BAYVIEW',14303]] 

# Create the pandas DataFrame 
df = pd.DataFrame(data, columns = ['Neighborhood', 'Count']) 
print(df)

world_map = folium.Map(location=[0,0], zoom_start=2, tiles='Mapbox Bright')

world_map.choropleth(
    geo_data="/home/sean/software/coursera/IBM_Data_Science/Data_Visualization_with_Python/final_project/IBM_Data_Science_Specialization/san-francisco.geojson",
    data=data,
    columns=['Neighborhood', 'Count'],
   
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Crime Rates'
)
print(world_map)


  