
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url="https://the-internet.herokuapp.com/login"

driver=webdriver.Chrome()
driver.get(url)
usuario=driver.find_element(By.ID, "username")
pwd=driver.find_element(By.ID, "password")
boton=driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
usuario.send_keys("tomsmith")
pwd.send_keys("SuperSecretPassword!")
boton.click()
espera=WebDriverWait(driver,10)
mensaje=espera.until(EC.visibility_of_element_located((By.ID, "flash")))
print(mensaje.text)
driver.quit()
