# This part of course its outdated... So I used a tip from a student on course, he uses telegram insted od twilio, he uses the following documentation: https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e

import requests
import time
import schedule


def get_weather():
    MY_LAT = 000000000
    MY_LONG = 00000000
    API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"

    parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": API_KEY,
        "cnt": 4,
    }

    try:
        response = requests.get(
            url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
        response.raise_for_status()
        weather_data = response.json()

        will_rain = False
        if "list" in weather_data:
            for hour_data in weather_data["list"]:
                condition_code = hour_data["weather"][0]["id"]
                if int(condition_code) < 700:
                    will_rain = True
                    break

        return will_rain

    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return False
    except KeyError as e:
        print("KeyError:", e)
        return False


def telegram_bot_sendtext(bot_message):
    bot_token = 'YOUR_BOT_TOKEN'
    bot_chatID = 'YOUR_CHAT_ID'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


def report():
    if get_weather():
        telegram_bot_sendtext("Bring an umbrella! Will rain.")
    else:
        telegram_bot_sendtext("No need for an umbrella. It won't rain.")


schedule.every().day.at("12:00").do(report)

while True:
    schedule.run_pending()
    time.sleep(1)
