from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

link = "http://suninjuly.github.io/selects2.html"
num1 = "num1"
num2 = "num2"
submit_button = "//button[@type='submit']"

driver.get(link)
x = driver.find_element(By.ID, num1).text
y = driver.find_element(By.ID, num2).text
z = int(x) + int(y)
select = Select(driver.find_element(By.ID, 'dropdown'))
select.select_by_value(str(z))
driver.find_element(By.XPATH, submit_button).click()


