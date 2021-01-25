# import web driver
from time import sleep
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# defining new variable passing two parameters
#writer = csv.writer(open('/Users/student/Desktop/LinkedIn_Scraping/linkedin_scrap.xlsx', 'w'))

# writerow() method to the write to the file object
#writer.writerow(['Name', 'Job Title', 'Company', 'College', 'Location', 'URL'])

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('/Users/student/Desktop/LinkedIn_Scraping/chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')


username = driver.find_element_by_class_name('input__input')

username.send_keys('adamelshimi1234@hotmail.co.uk')

password = driver.find_element_by_id('session_password')

password.send_keys('egypt44life88')

log_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')

log_in_button.click()
sleep(0.5)

driver.get('https:www.google.com')
sleep(3)

search_query = driver.find_element_by_name('q')
search_query.send_keys('site:linkedin.com/in/ AND "python developer" AND "London"')
sleep(0.5)

search_query.send_keys(Keys.RETURN)
sleep(3)

Linkedin_url = driver.find_elements_by_tag_name('cite')
linkedin_urls = [url.text for url in linkedin_urls]
sleep(0.5)

driver.quit()
