import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time
import re
from pprint import pprint

import json


drop_cols = ['statefp', 'countyfp', 'countyns', 'geoid', 'lsad', 'classfp', 'mtfcc', 'csafp', 'metdivfp', 'funcstat', 'aland', 'awater', 'intptlat', 'intptlon', 'countyfp_nozero']

state_list = ['ga-county-boundaries', 'la-county-boundaries', 'ms-county-boundaries','nc-county-boundaries','sc-county-boundaries','tn-county-boundaries','tx-county-boundaries','va-county-boundaries']

# taking in state specific file name as a string, 
#it's not working but i need to move on. i'd like to come back to this eventually
def county_boundary_remake(state_list, drop_cols):
    for state in state_list:
        with open(f'state_county_boundaries/{state}.geojson') as f:
            data = json.load(f)

        for c in range(len(data['features'])):
            for col in drop_cols:
                print('dropping', data['features'][c]['properties']['name'])
                del data['features'][c]['properties'][col]

        file_poly = f'state_county_boundaries/{state}-simp.geojson'

        with open(file_poly, 'w+') as f:
            json.dump(data, f)

#county_boundary_remake(state_list, drop_cols)

state_df = pd.read_csv("state_census/VA/VA_racial_census_simplified.csv")

def add_county_pop(state_list, state_df):
    count_name_list = state_df['County Name'].to_list()
    total_pop = state_df['Total Population'].to_list()
    pop_not_white = state_df['Total Population Not White'].to_list()
    pop_percentage = state_df['Percentage Not White'].to_list()
    with open(f'state_county_boundaries/va-county-boundaries-simp.geojson') as f:
        data = json.load(f)

    print(len(data['features']))
    for count in range(len(data['features'])):
        county_name = data['features'][count]['properties']['namelsad']
        indexer = count_name_list.index(county_name)

        #should eventually build in an if statement here

        data['features'][count]['properties']['total_population'] = total_pop[indexer]
        data['features'][count]['properties']['pop_not_white'] = pop_not_white[indexer]
        data['features'][count]['properties']['percent_not_white'] = str(pop_percentage[indexer])
        print(data['features'][count]['properties'])

        with open(f'state_county_boundaries/va-county-boundaries-pop.geojson', 'w+') as f:
            json.dump(data, f)
add_county_pop(state_list, state_df)  

    # for name in fl_count_name_list:
    #     if data['features'][c]['properties']['nameslad'] == name:
    #         print(name)

    # for count, name in enumerate(fl_count_name_list):
    #     print(name)
    #     if name == data['features'][count]['properties']['namelsad']:
    #         print(name, fl_total_pop[count]) 


    #data['features'][0]['properties']['total_population'] = '278468'