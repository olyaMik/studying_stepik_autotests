from selenium import webdriver
from selenium.webdriver.common.by import By
import math


driver = webdriver.Chrome()

link = "http://suninjuly.github.io/get_attribute.html"
x_locator = "img"
answer_field = "answer"
checkbox = "robotCheckbox"
radiobutton = "robotsRule"
submit_button = "//button[@type='submit']"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


driver.get(link)
x = driver.find_element(By.TAG_NAME, x_locator).get_attribute("valuex")
answer = calc(x)
driver.find_element(By.ID, answer_field).send_keys(answer)
driver.find_element(By.ID, checkbox).click()
driver.find_element(By.ID, radiobutton).click()
driver.find_element(By.XPATH, submit_button).click()

