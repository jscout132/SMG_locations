import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time
import re

#setting col names from the csv with slightly shorter names
col_names = [
    "Org Name",
    "Org Id",
    "Org Address 1",
    "Org City",
    "Org State",
    "Org Postal Code",
    "Full Address",
    "Applicant County",
    "Latitude",
    "Longitude",
]

# globally setting the dataframe from the csv with all address information
df = pd.read_csv("SMG_address.csv", names=col_names, skiprows=[0])
# removing limits on column with to prevent abbreviation
pd.set_option("display.max_colwidth", None)

# formatting and creating list of full addresses as opposed to split across multi cols
# completed, not needed to be run again
def full_address_format(df):
    full_addresses = []

    smg_full_addresses = df['Full Address'].to_list()
    smg_city_names = df['Org City'].to_list()

    for c, address in enumerate(smg_full_addresses):
        dig_check = re.findall("[0-9]", address[0])
        if dig_check:
            full_addresses.append(smg_full_addresses[c])
        else:
            full_addresses.append(smg_city_names[c])

    return full_addresses
# global_address = full_address_format(df)
# completed, not needed to be run again


# setting up Nominatim geopy instance
app = Nominatim(user_agent="SMG Address")


lat_list, lon_list = [], []

# function to take in the address list and append the lat and lon to their respective lists
# completed, not needed to be run again
def get_coord(addresses):
    for address in addresses:
        try:
            print(address)
            location = app.geocode(address).raw
            lat_list.append(location["lat"])
            lon_list.append(location["lon"])
            time.sleep(1.5)
        except GeocoderTimedOut:
            print('time out', address)
            time.sleep(5)
            
#get_coord(global_address)
# completed, not needed to be run again
