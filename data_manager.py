from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/07a7e7bf280a3a64f1981c17040f44ca/flightDeals/prices"
# SHEETY_API_KEY = "467b9ac81ba15124296e0f5c0e34226c"
# SHEETY_API_ID = "11dde921"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        # pprint(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

# dm = DataManager()
# print(dm.get_destination_data())