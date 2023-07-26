import os

import pandas as pd
from emodpy_malaria.weather import *
from emodpy_malaria.weather.weather_variable import WeatherVariable
import manifest


indir = os.path.join(manifest.input_dir,"example_weather")

df, wa = weather_to_csv(indir)
df.to_csv(os.path.join(indir, "output.csv")) # Make a copy of CSV for manipulation if needed

df1 = df.copy()
df1['date'] = pd.date_range('2019-01-01', '2019-12-31')
df1['nodes'] = 1

# Create EMOD-readable weather files to be used in simulations from modified CSVs if needed
#wa.update({"IdReference": "Custom user"}) #update ID reference if desired

weather_columns = {
    WeatherVariable.AIR_TEMPERATURE: "airtemp",
    WeatherVariable.RELATIVE_HUMIDITY: "humidity",
    WeatherVariable.RAINFALL: "rainfall",
    WeatherVariable.LAND_TEMPERATURE: "landtemp"
}
weather_filenames = {
    WeatherVariable.AIR_TEMPERATURE: "example_air_temperature_daily.bin",
    WeatherVariable.RELATIVE_HUMIDITY: "example_relative_humidity_daily.bin",
    WeatherVariable.RAINFALL: "example_rainfall_daily.bin",
    WeatherVariable.LAND_TEMPERATURE: "example_land_temperature_daily.bin"
}

csv_to_weather(df1, attributes=wa, weather_columns=weather_columns,
               weather_dir=os.path.join(indir, "out"),
               weather_file_names=weather_filenames)