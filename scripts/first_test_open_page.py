from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Укажите путь к веб-драйверу, если он не добавлен в PATH
# driver = webdriver.Chrome(executable_path="/path/to/chromedriver")

# Автоматически находит chromedriver, если он в PATH
driver = webdriver.Chrome()

# Headless режим: Для запуска тестов без открытия окна браузера можно использовать headless режим. Например, для Chrome:
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.google.com")
print(driver.title)
sleep(2)
driver.quit()