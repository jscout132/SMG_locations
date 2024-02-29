from flask import Flask, render_template

#from config import arc_gis_api, map_id

app = Flask(__name__)
app.debug = False

@app.route('/')
def home():
    return render_template('index.html')#, arc_gis_api=arc_gis_api, map_id=map_id)

