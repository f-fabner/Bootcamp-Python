from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Configurações para manter o navegador aberto após o fim do script
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to wikipedia
driver.get("http://secure-retreat-92358.herokuapp.com/")

#-------metodo que eu resolvi------
# Encontrando cada um dos imputs e colocando as coiass escritas
# imput01 = driver.find_element(By.XPATH, value="/html/body/form/input[1]")
# imput01.send_keys("Fernando")

# imput02 = driver.find_element(By.XPATH, value="/html/body/form/input[2]")
# imput02.send_keys("Silva")

# imput03 = driver.find_element(By.XPATH, value="/html/body/form/input[3]")
# imput03.send_keys("Fernando@silva.com")

# # Encontrando o botão e mandando clickar nele
# button = driver.find_element(By.XPATH, value="/html/body/form/button")
# button.click()


#-------metodo da professora------
# Finding first name, last name, and email fields
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

# Fill out the form
first_name.send_keys("Fernando")
last_name.send_keys("Silva")
email.send_keys("fernando@silva.com")

# Locate the "Sign Up" button. Then click on it
submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()


# Finaliza o driver
input("Pressione Enter para encerrar o script...")
driver.quit()


