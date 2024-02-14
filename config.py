import os
from dotenv import load_dotenv

load_dotenv()

arc_gis_api = os.getenv('arc_gis')
map_id = os.getenv('portal_id')

