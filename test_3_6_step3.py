from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import math


class Test_Fixtures_Param():

    links = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"]

    answer_field = "textarea"   # tag
    submit_button = "submit-submission"      # class
    result_message = "pre"    # tag

    @pytest.fixture()
    def setup_method(self):
        driver = webdriver.Chrome()
        return driver


    def answer_count(self):
        answer = math.log(int(time.time()))
        return answer


    @pytest.mark.parametrize('link', links)
    def test_param(self, setup_method, link):
        driver = setup_method
        driver.get(link)
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.TAG_NAME, self.answer_field)))
        answer = self.answer_count()
        driver.find_element(By.TAG_NAME, self.answer_field).send_keys(answer)
        driver.find_element(By.CLASS_NAME, self.submit_button).click()
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.TAG_NAME, self.result_message)))
        expected_message = "Correct!"
        actual_message = driver.find_element(By.TAG_NAME, self.result_message).text
        assert actual_message == expected_message, f"Smth went wrong: actual message is {actual_message}"









