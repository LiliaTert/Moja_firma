from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
import time

driver = webdriver.Chrome()
driver.get('https://app.moyafirma.org/#/auth/login')
driver.maximize_window()

# send an email in the "Email" field
email = 'tester06.qa.2022@gmail.com'
xpath_email_field = "//input[@type='email']"
WebDriverWait(driver, 100).until(EC.presence_of_element_located(('xpath', xpath_email_field)))
field_email = driver.find_element('xpath', xpath_email_field)
field_email.send_keys(email)
time.sleep(2)

# send a password in the "Password" field
password = 'As12345678*'
xpath_password_field = "//input[@type='password']"
WebDriverWait(driver, 100).until(EC.presence_of_element_located(('xpath', xpath_password_field)))
field_password = driver.find_element('xpath', xpath_password_field)
field_password.send_keys(password)
time.sleep(2)

# choose the "Remember me" check-box
xpath_remember_me_check_box = "//span[text()='Remember me']"
WebDriverWait(driver, 100).until(EC.presence_of_element_located(('xpath', xpath_remember_me_check_box)))
remember_me_check_box = driver.find_element('xpath', xpath_remember_me_check_box)
remember_me_check_box.click()
time.sleep(2)

# click the "Sign in" button"
xpath_button_submit = "//button[@type='submit']"
WebDriverWait(driver, 100).until(EC.presence_of_element_located(('xpath', xpath_button_submit)))
button_submit = driver.find_element('xpath', xpath_button_submit)
button_submit.click()
time.sleep(2)
