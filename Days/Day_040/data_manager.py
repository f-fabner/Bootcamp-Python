import os
import requests

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.sheety_prices_endpoint = os.environ.get('SHEETY_PRICES_ENDPOINT')
        self.sheety_users_endpoint = os.environ.get('SHEETY_USERS_ENDPOINT')

    def get_destination_data(self):
        response = requests.get(url=self.sheety_prices_endpoint)
        data = response.json()
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
                url=f"{self.sheety_prices_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=self.sheety_users_endpoint)
        data = response.json()
        customer_emails = [user["email"] for user in data["users"]]
        return customer_emails
