from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from util_func import linkd

load_dotenv()
driver = webdriver.Firefox()

def main():
    linkd.login(driver)


if __name__ == '__main__':
    main()


    # driver.close()

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