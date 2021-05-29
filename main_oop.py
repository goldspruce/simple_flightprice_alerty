#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
import requests
from datetime import datetime, timedelta
import os
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

#exercise_text = input("Tell me which exercises you did: ")

#"b5931cb9"
#"b0926221d280d0c3d80f4fed08b0c099"
#export ID=b5931cb9; export KEY=b0926221d280d0c3d80f4fed08b0c099; python main.py

#APP_ID = os.environ["ID"]
#API_KEY = os.environ["KEY"]

sheet_endpoint = "https://api.sheety.co/c05c293f18cd6e084a1db612d2dc610c/flightDeals/prices"
sheet_endpoint = "https://api.sheety.co/251863ceff025d966c98c3a6e5e43fcf/flightDeals3/prices"

header = {
    "Content-Type": "application/json"
}

#sheet = requests.get(sheet_endpoint)#, headers=header_)
#print(sheet_r)
#print(sheet_r.text)
#print(sheet_r.json())

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
#pprint(sheet_data)

#sheet_test = requests.post(sheet_endpoint, json={"price":{"city":"los angeles"}})#, headers=header)
#print(sheet_test)

flight_search = FlightSearch()
notification_manager = NotificationManager()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    data_manager.update_destination_codes()


ORIGIN_CITY_IATA = "LON"

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    try:
    	if flight.price < destination["lowestPrice"]:
    		notification_manager.send_sms(
    			message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
    	else:
    		print("Not cheap enough")
    except:
    		print("No flights")