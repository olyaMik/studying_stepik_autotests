from selenium import webdriver
from selenium.webdriver.common.by import By


name = "//label[text()='First name:*']/parent::div/input"
surname = "//label[text()='Last name:*']/parent::div/input"
city = "//label[text()='City:*']/parent::div/input"
country = "//label[text()='Country:*']/parent::div/input"
submit_button = "//button[@type='submit']"

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/find_xpath_form")
driver.find_element(By.XPATH, name).send_keys("Madera")
driver.find_element(By.XPATH, surname).send_keys("Mikhailova")
driver.find_element(By.XPATH, city).send_keys("Kiev")
driver.find_element(By.XPATH, country).send_keys("Ukraine")
driver.find_element(By.XPATH, submit_button).click()


Form.form_filling()






