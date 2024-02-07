import pandas as pd
from geopy.geocoders import Nominatim
import time

col_names = ['Org Name','Org Id','Org Address 1','Org City','Org State','Org Postal Code','Full Address','Applicant County','Latitude','Longitude']


#globally setting the dataframe from the csv
df = pd.read_csv("SMG_address.csv", names=col_names, skiprows=[0])
#removing limits on column with to prevent abbreviation
pd.set_option('display.max_colwidth', None)

#formatting and creating list of full addresses 
def full_address_format(df):
    return [address.strip() for address in df['Full Address'].to_list()]

global_address = full_address_format(df)

app = Nominatim(user_agent="SMG Address")

lat_list, lon_list = [], []

# function to take in the address list and append the lat and lon to their respective lists
def get_coord(addresses):
    for address in addresses:
        location = app.geocode(address).raw
        lat_list.append(location["lat"])
        lon_list.append(location["lon"])
        time.sleep(1)

#get_coord(clean_address)


# updating CVS with coordinates
def adding_coords(smg_address, lat_list, lon_list):
    for count, address in enumerate(lat_list):
        smg_address.loc[count, "Latitude"] = lat_list[count]
        smg_address.loc[count, "Longitude"] = lon_list[count]
        smg_address.to_csv("SMG_address_test.csv", index=False)

#adding_coords(df, lat_list, lon_list)

address_list = [
    "1813 Winona Avenue, Montgomery, AL, 36107",
    "2100 4th Ave N, Birmingham, AL, 35203",
    "1023 SHADY LANE CIR, TALLADEGA, AL, 35160",
    "112 Steele Street, Huntsville, AL, 35801",
    "7956 Vaughn Rd PMP# 180, Montgomery, AL, 36116",
    "200 Town Madison Blvd, Madison, AL, 35758",
    "7500 Bellaire Blvd, Houston, TX, 77036",
    "5310 Lenox Ave Ste 22, Jacksonville, FL, 32205",
    "37240 Lock Street, Dade City, FL, 33523",
    "5715 White Hickory Cir, Tamarac, FL, 33319",
    "P.O. Box 1911, Orlando, FL, 32801",
    "1400 Clay Ave SW, Cairo, GA, 39828",
    "1064 Desota Street, GAINESVILLE, GA, 30501",
    "1003 Pineview Drive, Valdosta, GA, 31602",
    "402 Colton Avenue, Thomasville, GA, 31792",
    "11632 DAVENPORT LN, JOHNS CREEK, GA, 30005",
    "5680 Oakbrook Parkway Suite 145, Norcross, GA,...",
    "1305 BARNARD STREET POBOX 651, Savannah, GA, 3...",
    "1520 Thomas H. Delpit Dr, Baton Rouge, LA, 70802",
    "2900 Westfork Drive, Baton Rouge, LA, 70827",
    "708 Falcon Ave., Sicily Island, LA, 71368",
    "6803 Press Dr Ste 160/162, New Orleans, LA, 70126",
    "1120 Government Street Bldg. E, Baton Rouge, L...",
    "2818 Monroe Street, New Orleans, LA, 70118",
    "610 Head Start Street, Duck Hill, MS, 38925",
    "400 CENTRAL AVENUE SUITE 105, LAUREL, MS, 39441",
    "108 Horseshoe Circle, Jackson, MS, 39203",
    "157 Rockbridge Circle, Clinton, MS, 39056",
    "P.O. Box 141, Duck Hill, MS, 38925",
    "501 West County Line rd, Suite C, Tougaloo, MS...",
    "P.O. Box 11437, Jackson, MS, 39283",
    "1339 19th Street, Gulfport , MS, 39501",
    "2981 lollars grove road, Eupora, MS, 39744",
    "200 N Congress Street, Jackson, MS, 39201",
    "611 Summit Ave. Suite 10, Greensboro, NC, 27405",
    "P.O. Box 2333, Burlington, NC, 27216",
    "3509 Haworth Dr. Ste. 306, RALEIGH, NC, 27609",
    "508 N. Grove Street, Hendersonville, NC, 28792",
    "943 S. Park St, Asheboro, NC, 27203",
    "PO BOX 1391, Reidsville, NC, 27323",
    "711 Hillsborough Street, Suite 102, Raleigh, N...",
    "505 swann dr, Lumberton, NC, 28358",
    "3220 Burntwood Circle, Raleigh, NC, 27610",
    "25805 Andrew Jackson Hwy, Delco, NC, 28436",
    "Po Box 2134, Wilson, NC, 27893",
    "3724 National Dr Suite 100, Raleigh, NC, 27612",
    "PO Box 805, Kinston, NC, 28502",
    "PO Box 37374, Raleigh, NC, 27627",
    "1408 Hillsborough Street, Raleigh, NC, 27605",
    "P.O. Box 12102, Winston Salem, NC, 27117",
    "1408 Hillsborough St, Raleigh, NC, 27605",
    "P.O. Box 403, Fayetteville, NC, 28312",
    "2633 White Oak Dr, Burlington, NC, 27215",
    "3326 Durham-Chapel Hill Blvd, Durham, NC, 27770",
    "2 Aubrey Circle, Sumter, SC, 29153",
    "Post Office Box 71502, North Charleston, SC, 2...",
    "825 Bleeker Lane, West Columbia, SC, 29619",
    "PO Box 7187, Columbia, SC, 29201",
    "355 Faulkner Dr, Moore, SC, 29369",
    "P O Box 50055, Columbia, SC, 29250",
    "1112 Mason Hill Way, Spartanburg, SC, 29301",
    "2816 Pinebrook Trail, Antioch , TN, 37013",
    "701 Murfreesboro Pike, Nashville, TN, 37210",
    "3310 Ezell Red, Nashville, TN, 37211",
    "8220 EAST SHELBY DRIVE, MEMPHIS, TN, 38125",
    "PO Box 5503, Chattanooga, TN, 37406",
    "6957 Tiffany Lane, Chattanooga, TN, 37412",
    "3620 Buena Vista Pike Suite E, Nashville, TN, ...",
    "P O Box 3226, Chattanooga, TN, 37404",
    "P.O. Box 331144, Nashville, TN, 37203",
    "1808 S Good Latimer Expressway, Dallas, TX, 75226",
    "1415 Dakota St, El Paso, TX, 79930",
    "221 W. Twickenham Trl, Houston, TX, 77076",
    "1809 Hollister St. Suite C202, Houston, TX, 77080",
    "4530 W. 34th Street, Houston, TX, 77092",
    "1104 Lupo Dr, Dallas, TX, 75207",
    "5841 Berkshire, Dallas, TX, 75209",
    "417 S. Ohio Ave, Mercedes, TX, 78570",
    "3846 River Falls, San Antonio, TX, 78259",
    "6715 Little River Turnpike, Annandale, VA, 22003",
    "PO Box 8042, Alexandria, VA, 22306",
    "12703 Longleaf Lane, Herndon, VA, 20170",
]
