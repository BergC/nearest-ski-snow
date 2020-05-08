# Dependencies
import requests

# Files
from mountains import mountains

# Functions
def build_three_day_forecast(mountains):
    '''
    Ping Dark Sky API and format weather forecast information.
    '''

    data_refined = {}

    # Make API request
    for mountain_tuple in mountains['washington']:
        r = requests.get(f'https://api.darksky.net/forecast/0b0a022827ec5a66ef1c53e946532915/{mountain_tuple[1]}').json()


        data = r['daily']['data']

        data_refined.update({ mountain_tuple[0]: [] })

        weather_count = 0

        while weather_count < 3:
            data_refined[mountain_tuple[0]].append(
                {
                    'time': data[weather_count]['time'],
                    'precip_type': data[weather_count]['precipType'],
                    'precip_probability': data[weather_count]['precipProbability'],
                    'precip_intensity': data[weather_count]['precipIntensity'],
                    'precip_intensity_max': data[weather_count]['precipIntensityMax'],
                    'precip_intesntiy_max_time': data[weather_count]['precipIntensityMaxTime'],
                    'min_temp': data[weather_count]['temperatureMin'],
                    'max_temp': data[weather_count]['temperatureMax']                    
                }
            )

            weather_count += 1

    print(data_refined)


build_three_day_forecast(mountains)
