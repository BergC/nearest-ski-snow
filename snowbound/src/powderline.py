import requests

def snow_quality_change(mountain):
    '''
    Use the Powderlines API to ping SNOTEL station data for last 3 days snow pack and changes.
    '''

    lat,lon = mountain[1].split(',')

    r = requests.get(f'http://api.powderlin.es/closest_stations?lat={lat}&lng={lon}&data=true&days=2&count=3').json()

    for snotel_station in r:
        if len(snotel_station['data']) > 1:
            return snotel_station
            break


if __name__ == "__main__":
    mountain = ('mount_baker', '48.858511,-121.665897')
    
    print(snow_quality_change(mountain))
