from selenium import webdriver


def get_title():
    driver = webdriver.Chrome()
    driver.get('https://www.linkedin.com')
    print(driver.title)
    driver.close()


get_title()