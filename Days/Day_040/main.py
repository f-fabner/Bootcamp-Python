from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import TelegramNotificationManager

load_dotenv()

bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
chat_id = os.environ.get('TELEGRAM_CHAT_ID')
origin_city_iata = os.environ.get('ORIGIN_CITY_IATA')

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

if sheet_data:
    flight_search = FlightSearch()
    notification_manager = TelegramNotificationManager()

    if sheet_data[0]["iataCode"] == "":
        for row in sheet_data:
            row["iataCode"] = flight_search.get_destination_code(row["city"])
        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()

    tomorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

    for destination in sheet_data:
        flight = flight_search.check_flights(
            origin_city_iata,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today
        )
        if flight and flight.price < destination["lowestPrice"]:
            notification_manager.send_message(
                f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            )
else:
    print("Failed to fetch destination data.")
