from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import pytest

class Test_Registration(unittest.TestCase):

    name_field = "//label[text()='First name*']/following-sibling::input"
    surname_field = "//label[text()='Last name*']/following-sibling::input"
    email_field = "//label[text()='Email*']/following-sibling::input"
    submit_button = "//button[@type='submit']"
    success_text = "Congratulations! You have successfully registered!"

    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"

    def test_registration1(self):
        driver = webdriver.Chrome()
        driver.get(self.link1)
        driver.find_element(By.XPATH, self.name_field).send_keys("Albert")
        driver.find_element(By.XPATH, self.surname_field).send_keys("Einstein")
        driver.find_element(By.XPATH, self.email_field).send_keys("albert@gmail.com")
        driver.find_element(By.XPATH, self.submit_button).click()
        success_message = driver.find_element(By.TAG_NAME, "h1").text
        assert success_message == self.success_text, "Smth went wrong"

    def test_registration2(self):
        driver = webdriver.Chrome()
        driver.get(self.link2)
        driver.find_element(By.XPATH, self.name_field).send_keys("Albert")
        driver.find_element(By.XPATH, self.surname_field).send_keys("Einstein")
        driver.find_element(By.XPATH, self.email_field).send_keys("albert@gmail.com")
        driver.find_element(By.XPATH, self.submit_button).click()
        success_message = driver.find_element(By.TAG_NAME, "h1").text
        assert success_message == self.success_text, "Smth went wrong"



