import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# базовый url
base_url = "https://demoqa.com/radio-button"

# добавить опции/оставить браузер открытым
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())

# открытие браузера с параметрами
driver_chrome = webdriver.Chrome(
    options=options,
    service=service
)

# переход по url в браузере/развернуть на весь экран
driver_chrome.get(base_url)
driver_chrome.maximize_window()

# выбирает радио-баттон
radio_button = driver_chrome.find_element(By.XPATH, "(//label[@class='custom-control-label'])[2]")
radio_button.click()

time.sleep(2)
# проверяет радио-баттон
print(not radio_button.is_selected())# метод is_selected не работает на данном сайте
print("Радио-баттон выбран")