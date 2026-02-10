from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager  
import time

# Настройка драйвера Firefox

option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled', False)
option.set_preference('dom.webnotifications.enabled', False)
option.set_preference('media.volume_scale', 0.0)

browser = webdriver.Firefox()
browser.get("https://ya.ru/")
time.sleep(4)
browser.get("https://rutube.ru/?ysclid=mlh5vxo3b8603572134")
time.sleep(4)
browser.save_screenshot('manul1.png')
time.sleep(2)
browser.refresh()
time.sleep(2)

browser.quit()


