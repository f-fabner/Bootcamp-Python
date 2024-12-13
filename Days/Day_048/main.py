from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")

# price_reais = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_centavos = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"O preço é: {price_reais.text}.{price_centavos.text}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value="documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# driver.close()

# Localiza todos os itens da lista de eventos
event_items = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li')

# Extrai os dados para um dicionário no formato solicitado
events = {}
for index, item in enumerate(event_items):
    event_date = item.find_element(By.XPATH, './/time').text  # Data do evento
    event_name = item.find_element(By.XPATH, './a').text  # Nome do evento
    events[index] = {"time": event_date, "name": event_name}

# Exibe o dicionário final
print(events)

# Finaliza o driver

input("Pressione Enter para encerrar o script...")
driver.quit()


