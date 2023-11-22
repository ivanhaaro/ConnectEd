from selenium import webdriver
import sys

def getlatlong(place):
    
    driver = webdriver.Chrome("chromedriver.exe")
    
    driver.get("https://google.com")

    # Buscamos la página
    buscador = driver.find_element_by_id("APjFqb")
    buscador.send_keys("coordenadas-gps")

    buttonElement = driver.find_element_by_name("btnK")
    buttonElement.click()

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

    input.send_keys(place + "Latitude and Longitude" + Keys.ENTER)

    coordinates = driver.find_element_by_xpath