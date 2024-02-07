import pandas as pd
from geopy.geocoders import Nominatim
import time


df = pd.read_csv("SMG_address.csv")


def combine_address(row):
    return f"{row['Organization Address 1']}, {row['Organization City']}, {row['Organization State']}, {row['Organization Postal Code']}"


address_list = df.apply(lambda row: combine_address(row), axis=1)

# creating address list of strings
clean_address = [i[2:].lstrip() for i in address_list.to_string().split("\n")]
print(clean_address)


app = Nominatim(user_agent="SMG Address")

lat_list, lon_list = [], []


# function to take in the address list and append the lat and lon to their respective lists
def get_coord(addresses):
    for address in addresses:
        location = app.geocode(address).raw
        lat_list.append(location["lat"])
        lon_list.append(location["lon"])
        time.sleep(1)


get_coord(clean_address)


# updating CVS with coordinates
def adding_coords(smg_address, lat_list, lon_list):
    for count, address in enumerate(lat_list):
        smg_address.loc[count, "Latitude"] = lat_list[count]
        smg_address.loc[count, "Longitude"] = lon_list[count]
        smg_address.to_csv("SMG_address_test.csv", index=False)


adding_coords(df, lat_list, lon_list)

