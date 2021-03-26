from selenium import webdriver
import pytest
from locators import MAIN_PAGE_URL


@pytest.fixture(scope="function")
def chrome_drv():
    global driver
    driver = webdriver.Chrome(executable_path=r"C:/Users/Oks_Sunshine/Downloads/chromedriver_win32/chromedriver.exe")
    driver.maximize_window()  # maximize the page
    driver.implicitly_wait(30)


def srart_page(chrome_drv):
    driver.get(MAIN_PAGE_URL)


