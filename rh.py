import requests
import json
import subprocess

#server refers to mojio's api
apiURL = 'https://api.moj.io/v2/'
authToken = 'Bearer 53cab099-0e09-4454-8cb7-b9b4e42e4e53'


#Loads summary trip info from Mojio, returns 2d array (list) with summary data by trip
def loader():
    tripsJSON = getAllTrips()
    print(tripsJSON)
    allRelData = [] #list for final storage of all relevant data
    for trip in tripsJSON["Data"]:
        #Trip ID // Start City // End City // Start Timestamp // Distance[m] // Fuel Efficiency[km/L]// Vehicle ID
        #Exceptions for if no usable address data
        try:
            StartLocation = trip["StartLocation"]["Address"]["City"]
        except:
            StartLocation = "Somewhere"
        try:
            EndLocation = trip["EndLocation"]["Address"]["City"]
        except:
            EndLocation = "Somewhere"

        relevantDataList = [trip["Id"],
                            StartLocation,
                            EndLocation,
                            trip["StartTimestamp"],
                            trip["Distance"]["Value"],
                            trip["FuelEfficiency"]["Value"],
                            trip["VehicleId"]]
        allRelData.append(relevantDataList)
    return(allRelData)

def getFromAPI(url):
    headers = {'Authorization': authToken}
    print(url)
    return requests.get(url, headers=headers).content

def getAllTrips():
    endpoint = 'trips'
    url = apiURL + endpoint
    response = json.loads(getFromAPI(url))
    return response

def getEvents(tripID):
    url = apiURL + 'trips/' + tripID + '/history/states?top=9999'
    response = json.loads(getFromAPI(url))
    print(type(response))
    return response

def init():

    return 0