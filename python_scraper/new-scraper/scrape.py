import time, random
import bs4
import requests
from selenium import webdriver

browser = webdriver.Chrome('driver/chromedriver')
browser.get('https://www.linkedin.com/uas/login')
file = open('config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]


elementID = browser.find_element_by_id('username')
elementID.send_keys(username)

elementID = browser.find_element_by_id('password')
elementID.send_keys(password)

elementID.submit()

link = 'https://www.linkedin.com/in/rishabh-singh-61b706114/'
# link = 'https://www.linkedin.com/in/simran-gandhi-024593128/'
# link = 'https://www.linkedin.com/in/smriti-handa-0636045/'
# link = 'https://www.linkedin.com/in/charan-nadendla-858a17120/'
# link = 'https://www.linkedin.com/in/mayank-agrawal-1a5883148/'
browser.get(link)


SCROLL_PAUSE_TIME = 5

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

for i in range(3):
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break


src = browser.page_source
soup = bs4.BeautifulSoup(src, 'lxml')
soup    


# name_loc = name_div.find_all('ul')
# name = name_loc[0].find('li').get_text().strip()
# name

# loc = name_loc[1].find('li').get_text().strip()
# loc

# profile_title = name_div.find('h2').get_text().strip()
# profile_title

# connection = name_loc[1].find_all('li')
# connection = connection[1].get_text().strip()
# connection

# info = []
# info.append(link)
# info.append(name)
# info.append(profile_title)
# info.append(loc)
# info.append(connection)
# info

# exp_section = soup.find('section', {'id': 'experience-section'})
# exp_section

# exp_section = exp_section.find('ul')
# li_tags = exp_section.find('div')
# a_tags = li_tags.find('a')


# a_tags

