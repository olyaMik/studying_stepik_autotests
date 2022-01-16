from selenium import webdriver
from selenium.webdriver.common.by import By
import math


link = "http://suninjuly.github.io/execute_script.html"
x_locator = "input_value"
answer_field = "answer"
checkbox = "robotCheckbox"
radiobutton = "robotsRule"
submit_button = "//button[@type='submit']"

driver = webdriver.Chrome()
driver.get(link)
x = driver.find_element(By.ID, x_locator).text
answer = math.log(abs(12*math.sin(int(x))))
driver.find_element(By.ID, answer_field).send_keys(answer)
driver.find_element(By.ID, checkbox).click()
radiobutton_element = driver.find_element(By.ID, radiobutton)
driver.execute_script("return arguments[0].scrollIntoView(true);", radiobutton_element)
radiobutton_element.click()
driver.find_element(By.XPATH, submit_button).click()




