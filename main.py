from users_data_manager import UsersDataManager
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

print("Welcome to Teni's Flight Club.")
print("We find the best flight deals and email you.")
print("What is your first name?")
first_name = input()
print("What is your last name?")
last_name = input()

print("What is your email?")
email = input().lower()
print("Type your email again.")
email_confirmation = input().lower()

while not email == email_confirmation:
  print("The email you have provide is not the same, let's try again.")
  print("What is your email?")
  email = input()
  print("Type your email again.")
  email_confirmation = input()

users_data_manger = UsersDataManager()
users_data_manger.add_users(first_name, last_name, email)

print("Success! You're in the club!")

ORIGIN_CITY_IATA = "DUB"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    data_manager.city_codes = flight_search.get_destination_codes(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)

for destination_code in destinations:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is None:
            continue
    
    if flight.price < destinations[destination_code]["price"]:
        message = f"Subject:FlightClub: Cheap Flight\n\nLow price alert! Only €{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)

            link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_city}.{flight.out_date}*{flight.destination_city}.{flight.origin_airport}.{flight.return_date}"
            notification_manager.send_emails(message, link)
            
        
    
