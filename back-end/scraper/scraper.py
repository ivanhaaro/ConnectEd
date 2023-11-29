import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


def getlatlong2(place):

    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument('window-size=1920x1080')
    # chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
    driver = webdriver.Chrome(options=chrome_options)
    # Open the website
    driver.get('https://www.coordenadas-gps.com/')
    # wait = WebDriverWait(driver, 10)

    direccionTextBox = driver.find_element(by = By.ID, value="address")
    direccionTextBox.clear()
    direccionTextBox.send_keys(place)

    # Clicamos y Buscamos
    buttonElement = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[3]/div[1]/form[1]/div[2]/div/button")
    buttonElement.click()

    # Obtenemos los datos
    latitudElement = driver.find_element(by = By.ID, value="latitude")
    longitudElement = driver.find_element(by = By.ID, value="longitude")

    latitud = latitudElement.get_attribute("value")
    print(latitud)
    longitud = longitudElement.get_attribute("value")
    print(longitud)

    # Close the browser
    driver.quit()

    return latitud, longitud

def getlatlong(place):
    
    driver = webdriver.Chrome()
    
    driver.get("https://google.com")

    # Buscamos la página
    buscador = driver.find_element(by= By.ID, value="APjFqb")
    # buscador = driver.find_element("APjFqb")
    buscador.send_keys("coordenadas-gps")

    # buttonElement = driver.find_element(by= By.NAME, value="btnK")
    buscador.send_keys(Keys.ENTER)
    # buttonElement.click()

    # Entramos en la página
    stringId = driver.find_element_by_class_name("LC20lb MBeuO DKV0Md")
    stringId.click()

    # Buscamos la opción de poner la dirección, así chill
    direccionTextBox = driver.find_element_by_id("address")
    direccionTextBox.clear()
    direccionTextBox.send_keys("Massamagrell")

    # Clicamos y Buscamos
    buttonElement = driver.find_element_by_class("btn btn-primary")
    buttonElement.click()

    # Obtenemos los datos
    latitudElement = driver.find_element_by_id("latitude")
    longitudElement = driver.find_element_by_id("longitud")

    latitud = latitudElement.get_attribute("value")
    print(latitud)
    longitud = longitudElement.get_attribute("value")
    print(longitud)
    # input.send_keys(place + "Latitude and Longitude" + Keys.ENTER)

    coordinates = driver.find_element_by_xpath