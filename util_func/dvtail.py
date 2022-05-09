from time import sleep
from selenium.webdriver.common.by import By
import os


def login(driver):
    driver.get('https://dovetailapp.com')

    loginButton = driver.find_element(by=By.CSS_SELECTOR, value='.e10xq6bj0')
    
    login_field = driver.find_element(by=By.CSS_SELECTOR, value='.css-37k25f').send_keys(os.environ.get('DVTAIL_USERNAME'))
    sleep(0.1)
    
    password_field = driver.find_element(by=By.CSS_SELECTOR, value='#_recycled_uid1').send_keys(os.environ.get('DVTAIL_PASSWORD'))
    sleep(0.1)
    
    login_button = driver.find_element(by=By.CSS_SELECTOR, value='span.css-iei16y:nth-child(1)').click()


    # driver.close()

    return


# def search_jobs(driver):
#     jobs_link = driver.find_element(by=By.CSS_SELECTOR, value='global-nav__primary-link-text')
#     print(jobs_link)
#     return