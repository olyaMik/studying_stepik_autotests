from selenium import webdriver
from selenium.webdriver.common.by import By
import os

link = "http://suninjuly.github.io/file_input.html"
first_name = "firstname"
last_name = "lastname"
email = "email"
choose_file_button = "file"
submit_button = "//button[@type='submit']"

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "test.txt")

driver = webdriver.Chrome()
driver.get(link)
driver.find_element(By.NAME, first_name).send_keys("Clint")
driver.find_element(By.NAME, last_name).send_keys("Eastwood")
driver.find_element(By.NAME, email).send_keys("clinteastwood@gmail.com")
driver.find_element(By.ID, choose_file_button).send_keys(file_path)
driver.find_element(By.XPATH, submit_button).click()