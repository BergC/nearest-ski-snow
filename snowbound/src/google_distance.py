# Dependencies
import requests
import os

def mountain_qualification(filter_by, upper_bound, mountains, origin):
    '''
    Determine what mountains fall within desired distance or time-to-destination.
    '''

    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

    eligible_mountains = []

    for mountain_tuple in mountains['washington']:
            
        URL = f'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={origin}&destinations={mountain_tuple[1]}&key={GOOGLE_API_KEY}'

        r = requests.get(URL).json()

        # Google's distance matrix value is in meters. Multiply our miles by meters in a mile.
        if filter_by == 'distance' and r['rows'][0]['elements'][0]['distance']['value'] <= (upper_bound * 1609.34):
            eligible_mountains.append(mountain_tuple)
        elif filter_by == 'duration' and r['rows'][0]['elements'][0]['duration']['value'] <= upper_bound:
            eligible_mountains.append(mountain_tuple)

    return eligible_mountains


if __name__ == "__main__":
    print(mountain_qualification('distance', 300, mountains, '47.623550,-122.330974'))