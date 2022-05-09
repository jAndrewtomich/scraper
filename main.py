from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from util_func import linkd

load_dotenv()
driver = webdriver.Firefox()

def main():
    pass
















    # lk = linkd.LinkdObj(driver=driver)
    # lk.login()
    # lk.search_jobs() 

if __name__ == '__main__':
    main()