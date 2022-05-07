from time import sleep
from selenium.webdriver.common.by import By
import os


def login(driver):

    driver.get('https://linkedin.com')
    
    login_field = driver.find_element(by=By.ID, value='session_key').send_keys(os.environ.get('USERNAME'))
    sleep(0.1)
    
    password_field = driver.find_element(by=By.ID, value='session_password').send_keys(os.environ.get('PASSWORD'))
    sleep(0.1)
    
    login_button = driver.find_element(by=By.CLASS_NAME, value='sign-in-form__submit-button').click()
    sleep(0.1)

    return


def search_jobs(driver):
    jobs_link = driver.find_element(by=By.CSS_SELECTOR, values=)