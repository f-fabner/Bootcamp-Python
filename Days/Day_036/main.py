# Following day 35, I change the twilio for telegram...
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "YOUR OWN API KEY FROM ALPHAVANTAGE"
NEWS_API_KEY = "YOUR OWN API KEY FROM NEWSAPI"

def get_stock_data():
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": STOCK_API_KEY,
    }

    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]

    yesterday_data = data_list[0]
    yesterday_closing_price = float(yesterday_data["4. close"])

    day_before_yesterday_data = data_list[1]
    day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

    difference = yesterday_closing_price - day_before_yesterday_closing_price
    up_down = "🔺" if difference > 0 else "🔻"
    diff_percent = round((difference / yesterday_closing_price) * 100, 2)

    return up_down, diff_percent

def get_news():
    if abs(diff_percent) > 1:
        news_params = {
            "apiKey": NEWS_API_KEY,
            "qInTitle": COMPANY_NAME,
        }

        news_response = requests.get(NEWS_ENDPOINT, params=news_params)
        articles = news_response.json()["articles"]
        return articles[:3]
    else:
        return []

def format_message(up_down, diff_percent, articles):
    if not articles:
        return f"{STOCK_NAME}: {up_down}{diff_percent}%\nNo news available."
    
    formatted_articles = []
    for article in articles:
        formatted_article = f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
        formatted_articles.append(formatted_article)
    
    return formatted_articles

def send_telegram_message(bot_message):
    bot_token = 'YOUR_BOT_TOKEN'
    bot_chatID = 'YOUR_CHAT_ID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

if __name__ == "__main__":
    up_down, diff_percent = get_stock_data()
    articles = get_news()
    message = format_message(up_down, diff_percent, articles)
    
    if message:
        if isinstance(message, list):
            for msg in message:
                send_telegram_message(msg)
        else:
            send_telegram_message(message)
