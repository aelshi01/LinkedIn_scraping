# import web driver
from selenium import webdriver

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('/Users/username/bin/chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')


username = driver.find_element_by_class_name('input__input')

username.send_keys('adamelshimi1234@hotmail.co.uk')

password = driver.find_element_by_id('session_password')

password.send_keys('egypt44life88')

log_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')

log_in_button.click()