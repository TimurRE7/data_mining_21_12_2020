from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
    browser = webdriver.Firefox()
    url = 'https://www.zillow.com/san-francisco-ca/'
    browser.get(url)
    print(1)
