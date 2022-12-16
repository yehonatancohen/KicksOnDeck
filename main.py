from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the text file containing the proxies
with open("proxies.txt", "r") as f:
    proxies = f.readlines()

# Set the capabilities for the webdriver
capa = DesiredCapabilities.CHROME

# Loop through each proxy in the list
for proxy in proxies:
    # Set the proxy for the webdriver
    capa["proxy"] = {
        "proxyType": "MANUAL",
        "httpProxy": proxy,
        "ftpProxy": proxy,
        "sslProxy": proxy
    }

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # Create a new instance of the webdriver with the proxy
    driver = webdriver.Chrome(desired_capabilities=capa, options=options)

    # Use the webdriver as you normally would
    driver.get("https://www.nike.com/il/launch/t/air-jordan-1-low-travis-scott-black-phantom")

    buy_button = (By.XPATH, "//*[@id=\"root\"]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/div/button")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(buy_button))

    size_button = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[14]/button") 
    size_button.click()

    buy_button = driver.find_element(buy_button)
    buy_button.click()
