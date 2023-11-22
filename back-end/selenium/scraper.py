from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

def getlatlong(place):
    
    driver = webdriver.Chrome("chromedriver.exe")
    
    driver.get("https://google.com")

    input = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')

    input.send_keys(place + "Latitude and Longitude" + Keys.ENTER)

    coordinates = driver.find_element_by_xpath