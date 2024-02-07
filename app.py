import pandas
from geopy.geocoders import Nominatim
import time


df = pandas.read_csv('SMG_address.csv')

def combine_address(row):
    return f"{row['Organization Address 1']}, {row['Organization City']}, {row['Organization State']}, {row['Organization Postal Code']}"

address_list = df.apply(lambda row: combine_address(row), axis=1)

clean_address = [i[2:].lstrip() for i in address_list.to_string().split('\n')]



app = Nominatim(user_agent='SMG Address')
for address in clean_address:
    location = app.geocode(address).raw
    print(location['lat'])

def get_location_by_address(address):
    """This function returns a location as raw from an address
    will repeat until success"""
    time.sleep(1)
    try:
        return app.geocode(address).raw
    except:
        return get_location_by_address(address)