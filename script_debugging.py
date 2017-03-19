import rh
import views
import ipdb
from flask import Flask
app = Flask(__name__)

rh.sendEmail("joren.Jackson@gmail.com", 14, 5.66, "K. Fab")

trips = rh.loader()
Home = views.generateHomePage(trips)

#myTrip = 0
#fuelConsumed = trips['Data'][myTrip]['StartFuelLevel']['Value'] - trips['Data'][0]['EndFuelLevel']['Value']

rh.getEvents('dfa04b28-3882-49a9-8cb6-8fd6f6163885')



# ipdb.set_trace() #for debug
#print(rh.nodePort)


initialized = False

@app.route("/")
def hello():
    return views.generateHomePage(trips)

if __name__ == "__main__":
    app.run()
