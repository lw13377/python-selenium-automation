from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/-/es/ap/signin?openid.pape.max_auth_age=3600&openid.return_to=https%3A%2F%2Fwww.'
           'amazon.com%2Fmyh%2Fhouseholds%3Flanguage%3Des&openid.identity=http%3A%2F%2Fspecs.openid.net%2'
           'Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&langu'
           'age=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns'
           '=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')


driver.find_element(By.CSS_SELECTOR, "[aria-label='Amazon']")
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
driver.find_element(By.CSS_SELECTOR, ".a-form-label")
driver.find_element(By.CSS_SELECTOR, "#ap_email")
driver.find_element(By.CSS_SELECTOR, "input#continue")
driver.find_element(By.CSS_SELECTOR, "a[href*='signin_notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR, "a[href*='signin_notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR, ".a-expander-prompt")
driver.find_element(By.CSS_SELECTOR, "#ab-sign-in-ingress-link")
driver.find_element(By.CSS_SELECTOR, "#createAccountSubmit")


sleep(3)

