import math
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
link = "http://suninjuly.github.io/find_link_text"

driver.get(link)
link_needed = str(math.ceil(math.pow(math.pi, math.e)*10000))
driver.find_element(By.LINK_TEXT, link_needed).click()

name = "//label[text()='First name:*']/parent::div/input"
surname = "//label[text()='Last name:*']/parent::div/input"
city = "//label[text()='City:*']/parent::div/input"
country = "//label[text()='Country:*']/parent::div/input"
submit_button = "//button[@type='submit']"

driver.find_element(By.XPATH, name).send_keys("Madera")
driver.find_element(By.XPATH, surname).send_keys("Mikhailova")
driver.find_element(By.XPATH, city).send_keys("Kiev")
driver.find_element(By.XPATH, country).send_keys("Ukraine")
driver.find_element(By.XPATH, submit_button).click()
