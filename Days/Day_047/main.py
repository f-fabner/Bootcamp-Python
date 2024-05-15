import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

class AmazonPriceTracker:
    def __init__(self, url, target_price):
        self.url = url
        self.target_price = target_price

    def track_price(self):
        # Defina o cabeçalho para a solicitação HTTP
        header = {
            "your header"
        }

        # Faça a solicitação HTTP para a URL do produto
        try:
            r = requests.get(url=self.url, headers=header)
            r.raise_for_status()
        except requests.RequestException as e:
            print(f"Erro ao fazer a solicitação HTTP: {e}")
            return

        # Analise o conteúdo HTML da página do produto
        soup = BeautifulSoup(r.text, "html.parser")

        # Extraia o preço e o título do produto
        try:
            price_text = soup.find("span", class_="a-offscreen").text.strip()
            price_text = price_text.replace('R$', '').replace('.', '').replace(',', '.')
            price = float(price_text)
            title = soup.find("span", id='productTitle').text.strip()
        except AttributeError:
            print("Erro ao extrair informações do produto. Verifique se os seletores estão corretos.")
            return
        except ValueError as e:
            print(f"Erro ao converter o preço: {e}")
            return

        # Verifique se o preço é menor que o preço alvo e envie uma mensagem pelo Telegram
        if price < self.target_price:
            telegram_manager = TelegramNotificationManager()
            message = f"O preço de {title} está agora R${price}."
            telegram_manager.send_message(message)
        else:
            print(f"O preço atual ({price}) não é menor que o preço alvo ({self.target_price}).")

class TelegramNotificationManager:
    def __init__(self):
        # Carregue as variáveis de ambiente do arquivo .env
        load_dotenv()

        # Obtenha o token do bot e o chat ID das variáveis de ambiente
        self.bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.chat_id = os.getenv('TELEGRAM_CHAT_ID')

    def send_message(self, message):
        # Certifique-se de que o token do bot e o chat ID foram encontrados
        if self.bot_token is None or self.chat_id is None:
            print("Erro: Token do bot ou chat ID não encontrados nas variáveis de ambiente.")
            return

        send_text = f"https://api.telegram.org/bot{self.bot_token}/sendMessage?chat_id={self.chat_id}&parse_mode=Markdown&text={message}"
        try:
            response = requests.get(send_text)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error sending Telegram message: {e}")
            return None

if __name__ == "__main__":
    # Defina a URL do produto da Amazon e o preço alvo
    url = "your url"

    target_price = 1500.00

    # Crie uma instância do rastreador de preços da Amazon
    amazon_tracker = AmazonPriceTracker(url, target_price)
    
    # Rastreie o preço do produto
    amazon_tracker.track_price()