import requests

SHEETY_USERS_ENDPOINT = "https://api.sheety.co/07a7e7bf280a3a64f1981c17040f44ca/flightDeals/users"

class UsersDataManager:

  # def __init__(self):
  #   self.users_data = {}

  # def store_users_data(self, first_name, last_name, email):
  #   self.users_data[email] = [first_name, last_name]

  def add_users(self, first_name, last_name, email):
    
    users_data = {
      "user" : {
      "firstName": first_name,
      "lastName": last_name,
      "email": email,
      }
    }
    
    response = requests.post(url=SHEETY_USERS_ENDPOINT, json=users_data)
    print(response.json())

  def get_users_emails(self):
    response = requests.get(url=SHEETY_USERS_ENDPOINT)
    rows = response.json()["users"]
    print(rows)
    emails = [user["email"] for user in rows]
    return emails
    