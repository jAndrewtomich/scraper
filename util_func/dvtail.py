from time import sleep
from selenium.webdriver.common.by import By
import os


class DvTailObj:

    def __init__(self, driver, maxListings=10, keyWord='python'):
        self.driver = driver
        self.maxListings = maxListings
        self.keyWord = keyWord
        self.listings = None


    def login(self):
        self.driver.get('https://linkedin.com')
        
        login_field = self.driver.find_element(by=By.ID, value='session_key').send_keys(os.environ.get('USERNAME'))
        sleep(0.1)
        
        password_field = self.driver.find_element(by=By.ID, value='session_password').send_keys(os.environ.get('PASSWORD'))
        sleep(0.1)
        
        login_button = self.driver.find_element(by=By.CLASS_NAME, value='sign-in-form__submit-button').click()
        sleep(0.1)

        return


    def search_jobs(self):
        jobs_link = self.driver.find_element(by=By.CSS_SELECTOR, value='global-nav__primary-link-text')
        print(jobs_link)
        return