from selenium import webdriver
from selenium.webdriver.common.by import By

name_field = "//label[text()='First name*']/following-sibling::input"
surname_field = "//label[text()='Last name*']/following-sibling::input"
email_field = "//label[text()='Email*']/following-sibling::input"
submit_button = ""

link1 = "http://suninjuly.github.io/registration1.html"
link2 = ""

driver = webdriver.Chrome()
driver.get(link1)

driver.find_element(By.XPATH, name_field).send_keys("Albert")
driver.find_element(By.XPATH, surname_field).send_keys("Einstein")
driver.find_element(By.XPATH, email_field).send_keys("albert@gmail.com")
driver.find_element(By.XPATH, submit_button).click()