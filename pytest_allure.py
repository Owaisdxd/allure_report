import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup_function():
    """
    Initializes the Selenium WebDriver and opens the target website.
    
    The function is executed before each test function to set up the environment.
    """
    global driver
    driver = webdriver.Chrome()
    driver.get('website')  # Replace 'website' with the actual URL
    driver.maximize_window()

def teardown_function():
    """
    Closes the Selenium WebDriver and performs cleanup after each test function.
    
    The function is executed after each test function to clean up the environment.
    """
    global driver
    time.sleep(5)
    driver.quit()

def cred():
    """
    Provides a list of tuples containing usernames and passwords for parameterized testing.
    
    Returns:
        list: A list of tuples where each tuple contains a username and password.
    """
    return [
        ('username1@email.com', 'passone'),
        ('username2@email.com', 'passtwo'),
        ('username3@email.com', 'passthree'),
        ('username4@email.com', 'passone'),
        ('username5@email.com', 'passtwo'),
        ('username6@email.com', 'passthree'),
        ('username1@email.com', 'passone'),
        ('username2@email.com', 'passtwo'),
        ('username3@email.com', 'passthree'),
        ('username4@email.com', 'passone'),
        ('username5@email.com', 'passtwo'),
        ('username6@email.com', 'passthree')
    ]

@pytest.mark.parametrize("username,password", cred())
def test_website(username, password):
    """
    Tests the login functionality of the website with multiple sets of credentials.
    
    Args:
        username (str): The username to be used for the login test.
        password (str): The password to be used for the login test.
    
    The function performs the following actions:
    1. Enters the provided username and password into the login form.
    2. Takes a screenshot of the result and attaches it to the Allure report.
    """
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
    time.sleep(4)
    allure.attach(driver.get_screenshot_as_png(), name="report", attachment_type=AttachmentType.PNG)

# Note:
# To access the Allure report, run the following command:
# allure serve allure-dir-path
