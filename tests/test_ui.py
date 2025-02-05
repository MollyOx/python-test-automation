from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # 需要提前安装 ChromeDriver
    driver.get("https://www.saucedemo.com/")  # 示例电商网站
    yield driver
    driver.quit()
'''
def test_login(setup):
    driver = setup
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    #页面没出现的时候等待
    driver.implicitly_wait(5)
    time.sleep(5)
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url
'''
def test_login_failed(setup):
    driver = setup
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "login-button").click()
    errorms= driver.find_element(By.TAG_NAME,"h3").text
    assert"Epic sadface: Password is required"in errorms,f"实际消息为:{errorms}"

