from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

load_dotenv()


def main():
    driver = webdriver.Firefox()

    driver.get('https://linkedin.com')
    element = driver.find_element(by=By.ID, value='session_key').send_keys(os.environ.get('USERNAME'))
    sleep(2)
    driver.close()

    # while input("Type 'n' to quit, any other key to continue.") != 'n':


    # response = requests.get('https://uh.edu')
    # response.raise_for_status())
    # htmlText = response.text

    # soup = BeautifulSoup(htmlText, 'lxml')

    # initiative = soup.find(id='uh-initiatives')

    # with open('out/initiative.txt', 'w') as writer:
    #     writer.write(initiative.prettify()) 
    
    # with open('out/soup.txt', 'w') as writer:
    #     writer.write(soup.prettify())


if __name__ == '__main__':
    main()

