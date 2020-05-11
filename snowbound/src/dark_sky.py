# Dependencies
import requests
import os

# Files
from mountains import mountains

# Functions
from google_distance import mountain_qualification
from powderline import snow_quality_change

def build_three_day_forecast(filter_by, upper_bound, qualified_mountains, origin):
    '''
    Ping Dark Sky API and format weather forecast information.
    '''

    DARK_SKY_KEY = os.environ.get('DARK_SKY_KEY')

    data_refined = {}

    # Determine which mountains meet search criteria before fetching weather data.
    qualified_mountains = mountain_qualification(filter_by, upper_bound, mountains, origin)

    # Fetch weather data.
    for mountain_tuple in qualified_mountains:
        data_refined.update({ mountain_tuple[0]: [] })

        snow_quality = snow_quality_change(mountain_tuple)

        data_refined[mountain_tuple[0]].append(snow_quality)

        r = requests.get(f'https://api.darksky.net/forecast/{DARK_SKY_KEY}/{mountain_tuple[1]}').json()

        # Dark Sky returns JSON format. Selecting the daily data only.
        data = r['daily']['data']

        # Only want 3 day forecast.
        weather_count = 0

        while weather_count < 3:
            # try:
                data_refined[mountain_tuple[0]].append(
                    {
                        'precip': data[weather_count]["precipType"],
                        'time': data[weather_count]['time'],
                        'precip_probability': data[weather_count]['precipProbability'],
                        'precip_intensity': data[weather_count]['precipIntensity'],
                        'precip_intensity_max': data[weather_count]['precipIntensityMax'],
                        'precip_intensity_max_time': data[weather_count]['precipIntensityMaxTime'],
                        'min_temp': data[weather_count]['temperatureMin'],
                        'max_temp': data[weather_count]['temperatureMax']                    
                    }
                )

                weather_count += 1
            # except :
            #     return 'There appears to be an issue. Please try again in a few minutes.'

    return data_refined


print(build_three_day_forecast('distance', 70, mountains, '47.623550,-122.330974'))
