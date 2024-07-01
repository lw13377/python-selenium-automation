from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.target.com/')
sleep(2)
driver.find_element(By.ID, 'search').send_keys('brownie mix')
sleep(2)

driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(2)

expected_search = 'brownie mix'

sleep(2)
real_search = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text

sleep(2)

assert expected_search in real_search, f"expected {expected_search} but got {real_search}"


print('search matched')