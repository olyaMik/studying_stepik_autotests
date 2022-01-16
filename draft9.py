from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import math


link = "http://suninjuly.github.io/explicit_wait2.html"
price_field = "price"     # id
book_button = "book"    # id
x_locator = "input_value"    # id
answer_field = "answer"    # id
submit_button = "//button[@type='submit']"

driver = webdriver.Chrome()
driver.get(link)
WebDriverWait(driver, 15).until(ec.text_to_be_present_in_element((By.ID, price_field), "$100"))
driver.find_element(By.ID, book_button).click()

x = driver.find_element(By.ID, x_locator).text
answer = math.log(abs(12*math.sin(int(x))))
driver.find_element(By.ID, answer_field).send_keys(answer)
driver.find_element(By.XPATH, submit_button).click()




