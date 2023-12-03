import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CoordinateScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.coordenadas-gps.com/')
        self.last_latitude = None
        self.last_longitude = None

    def getlatlong(self, place):
        direccionTextBox = self.driver.find_element(by=By.ID, value="address")
        direccionTextBox.clear()
        direccionTextBox.send_keys(place)

        buttonElement = self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[3]/div[1]/form[1]/div[2]/div/button")
        buttonElement.click()

        def has_coordinates_changed(driver):

            try:
                latitudElement = driver.find_element(by=By.ID, value="latitude")
                longitudElement = driver.find_element(by=By.ID, value="longitude")

                latitud = latitudElement.get_attribute("value")
                longitud = longitudElement.get_attribute("value")
            except:
                return False

            if latitud != self.last_latitude or longitud != self.last_longitude:
                self.last_latitude = latitud
                self.last_longitude = longitud
                return latitud, longitud
            else:
                return False

        wait = WebDriverWait(self.driver, 5)
        new_coordinates = wait.until(has_coordinates_changed)

        return new_coordinates

    def close(self):
        self.driver.quit()
