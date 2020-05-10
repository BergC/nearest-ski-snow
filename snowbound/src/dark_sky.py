# Dependencies
import requests
import os

# Files
from mountains import mountains

# Functions
from google_distance import mountain_qualification

def build_three_day_forecast(filter_by, upper_bound, mountains, origin):
    '''
    Ping Dark Sky API and format weather forecast information.
    '''

    DARK_SKY_KEY = os.environ.get('DARK_SKY_KEY')

    data_refined = {}

    # Determine which mountains meet search criteria before fetching weather data.
    mountains = mountain_qualification(filter_by, upper_bound, mountains, origin)

    # Fetch weather data.
    for mountain_tuple in mountains:
        r = requests.get(f'https://api.darksky.net/forecast/{DARK_SKY_KEY}/{mountain_tuple[1]}').json()

        data = r['daily']['data']

        data_refined.update({ mountain_tuple[0]: [] })

        weather_count = 0

        while weather_count < 3:
            # try:
                data_refined[mountain_tuple[0]].append(
                    {
                        'whatever': data[weather_count]["precipType"],
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


print(build_three_day_forecast('distance', 100, mountains, '47.623550,-122.330974'))
