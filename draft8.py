from selenium import webdriver
from selenium.webdriver.common.by import By
import math


link = "http://suninjuly.github.io/alert_accept.html"
first_button = "button"    # tag
x_locator = "input_value"    # id
answer_field = "answer"    # id
submit_button = "//button[@type='submit']"

driver = webdriver.Chrome()
driver.get(link)
driver.find_element(By.TAG_NAME, first_button).click()
confirm_modal = driver.switch_to.alert
confirm_modal.accept()

x = driver.find_element(By.ID, x_locator).text
answer = math.log(abs(12*math.sin(int(x))))
driver.find_element(By.ID, answer_field).send_keys(answer)
driver.find_element(By.XPATH, submit_button).click()




