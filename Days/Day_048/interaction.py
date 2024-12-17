from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Configurações para manter o navegador aberto após o fim do script
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
# # --------abaixo é para wikipedia em português brasil-----
# # Inicia o driver do Chrome
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal")

# # Aguardar até que o elemento que contém o número de artigos seja carregado
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mw-content-text"]/div[1]/div[1]/div/div[1]/table/tbody/tr/td[2]/div/p/b[1]')))

# # Extrair o texto que contém o número de artigos
# numero_artigos = element.text
# print(f"Número de artigos na Wikipédia: {numero_artigos}")

# --------abaixo é para wikipedia em inglês-----
# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Hone in on anchor tag using CSS selectors
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)
# Daqui pra baixo aula 349
#article_count.click()

# Find element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the "Search" <input> by Name
search = driver.find_element(By.NAME, value="search")
# Sending keyboard input to Selenium
search.send_keys("Python", Keys.ENTER)

# Finaliza o driver
input("Pressione Enter para encerrar o script...")
driver.quit()


