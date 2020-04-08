# TODO: Not getting all 25 results from the page.
# TODO: Create a function that will click through the pagination.  The active li has an active tag in the name, try using that to select the next element past it.
# TODO: Get rid of the excess time.sleeps and convert some of them to expected_conditions.

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# # from linkedin_secrets import secret



driver = webdriver.Chrome()
jobs_list = []
job_id = 0

# Items you can change for search phrases
search_phrase = 'Software Engineer'
search_date_posted_range = '24'
filter_index = 1
current_date = '2019-12-02'


def login():
    driver.get('https://www.linkedin.com')
    driver.find_element(By.CSS_SELECTOR, "[class*='nav__button-secondary']").click()
    time.sleep(2)
    driver.find_element(By.ID, 'username').send_keys(secret.USER_NAME)
    driver.find_element(By.ID, 'password').send_keys(secret.PASSWORD + Keys.ENTER)
    time.sleep(5)
    print('logged in')


def filter_search_by_experience_level():
    driver.find_element(By.XPATH, '//*[@aria-label="Filter results by: Experience Level"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'//*[@id="experience-level-facet-values"]//ul//li[{filter_index}]//label').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="experience-level-facet-values"]//button[2]').click()
    time.sleep(5)


def filter_by_date_posted(date_posted):
    driver.find_element(By.XPATH, '//*[@aria-label="Date Posted filter. Clicking this button displays all Date Posted filter options."]').click()
    time.sleep(5)
    if date_posted == '24':
        driver.find_element(By.XPATH, '//*[@id="date-posted-facet-values"]//li[1]/label').click()
    if date_posted == 'week':
        driver.find_element(By.XPATH, '//*[@id="date-posted-facet-values"]//li[2]/label').click()
    if date_posted == 'month':
        driver.find_element(By.XPATH, '//*[@id="date-posted-facet-values"]//li[3]/label').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="date-posted-facet-values"]//button[2]').click()
    time.sleep(5)


def add_jobs_to_list(jobs):
    global job_id
    for job in jobs:
        job.click()
        time.sleep(5)
        job_title = driver.find_element(By.XPATH, '//*[@class="jobs-details-top-card__content-container"]/a')
        job_dict = {'id': job_id, 'job_title': job_title.text, 'job_title_link': job_title.get_attribute('href')}
        if driver.find_elements(By.XPATH, '//*[@data-control-name="commute_module_anchor"]'):
            job_dict['job_location'] = driver.find_element(By.XPATH, '//*[@data-control-name="commute_module_anchor"]').text
        else:
            job_dict['job_location'] = driver.find_element(By.XPATH, '//*[@class="jobs-details-top-card__content-container"]//span[3]').text

        if driver.find_elements(By.XPATH, '//*[@class="jobs-details-top-card__company-url ember-view"]'):
            job_dict['company_name'] = driver.find_element(By.XPATH, '//*[@class="jobs-details-top-card__company-url ember-view"]').text
            job_dict['company_link'] = driver.find_element(By.XPATH, '//*[@class="jobs-details-top-card__company-url ember-view"]').get_attribute('href')
        else:
            job_dict['company_name'] = driver.find_element(By.XPATH, '//*[@class="jobs-details-top-card__company-info t-14 t-black--light t-normal mt1"]').text

        if driver.find_elements(By.XPATH, '//*[@data-control-name="jobdetails_profile_poster"]'):
            job_dict['posted_by_name'] = driver.find_element(By.XPATH, '//*[@class="jobs-poster__name t-14 t-black t-bold mb0"]').text
            job_dict['posted_by_link'] = driver.find_element(By.XPATH, '//*[@data-control-name="jobdetails_profile_poster"]').get_attribute('href')
        else:
            pass
        jobs_list.append(dict(job_dict))
        time.sleep(2)
        job_id += 1
        print(job_dict)


def scroll_to_pagination():
    pagination = driver.find_element(By.XPATH, '//*[@class="jobs-search-two-pane__pagination"]')
    time.sleep(5)
    ActionChains(driver).move_to_element(pagination).perform()
    time.sleep(5)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # driver.execute_script("arguments[0].scrollIntoView();", pagination)


def job_search():
    login()
    driver.find_element(By.XPATH, '//*[@id="jobs-nav-item"]').click()
    driver.find_element(By.XPATH, '//*[@class="jobs-search-box__text-input"]').send_keys(search_phrase)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@class="jobs-search-box__text-input"]').send_keys(Keys.ENTER)
    time.sleep(5)
    filter_search_by_experience_level()
    filter_by_date_posted(search_date_posted_range)
    scroll_to_pagination()
    links = WebDriverWait(driver, 20).until(
        # EC.presence_of_all_elements_located((By.XPATH, '//*[@class="jobs-search-results__list artdeco-list"]//li//div//h3//a'))
        EC.presence_of_all_elements_located((By.XPATH, '//*[@class="jobs-search-results__list artdeco-list"]//h3//a'))
    )
    add_jobs_to_list(links)
    print(f'links length: {len(links)}')
    print(f'job_list length: {len(jobs_list)}')
    driver.close()


job_search()