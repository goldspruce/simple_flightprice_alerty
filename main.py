#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
import requests
from datetime import datetime
import os
from flight_search import FlightSearch

#exercise_text = input("Tell me which exercises you did: ")

#"b5931cb9"
#"b0926221d280d0c3d80f4fed08b0c099"
#export ID=b5931cb9; export KEY=b0926221d280d0c3d80f4fed08b0c099; python main.py

APP_ID = os.environ["ID"]
API_KEY = os.environ["KEY"]

sheet_endpoint = "https://api.sheety.co/c05c293f18cd6e084a1db612d2dc610c/flightDeals/prices"
sheet_endpoint = "https://api.sheety.co/251863ceff025d966c98c3a6e5e43fcf/flightDeals3/prices"

header = {
    "Content-Type": "application/json"
}

sheet = requests.get(sheet_endpoint)#, headers=header_)
#print(sheet_r)
#print(sheet_r.text)
#print(sheet_r.json())

sheet_data = sheet.json()["prices"]
pprint(sheet_data)

#sheet_test = requests.post(sheet_endpoint, json={"price":{"city":"los angeles"}})#, headers=header)
#print(sheet_test)

row = 2
for each in sheet_data:
	iata = FlightSearch.get_destination_code(each["city"])
	print(iata)
	sheet_inputs = {
        "price": {
        	#"city": each["city"],
            "iataCode": iata,
            #"lowestPrice": each["lowestPrice"]
        }
    }
    
	print(sheet_inputs)
	#sheet_input = requests.post(sheet_endpoint, json=sheet_inputs)#, headers=header)
	sheet_input = requests.put(f"{sheet_endpoint}/{row}", json=sheet_inputs)#, headers=header)
	print(sheet_input)
	row += 1

#delete last row
sheet_input = requests.delete(f"{sheet_endpoint}/19", json=sheet_inputs)#, headers=header)
print(sheet_input)
