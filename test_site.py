from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path=r"C:/Users/Oks_Sunshine/Downloads"
                                              r"/chromedriver_win32/chromedriver.exe")
    driver.maximize_window()  # maximize the page


def open_site():
    time.sleep(3)
    GOTO_WEB= driver.get("https://www.booking.com/index.html?label=gen173nr-"
               "1DCAEoggI46AdIM1gEaOkBiAEBmAEhuAEXyAEM2AED6AEBiAIBqAIDuALh7-"
               "uCBsACAdICJGYxZDgxZThiLTZjZDQtNDk1Mi05ZDcwLWQwN2Q4OTZjODA3NtgCBOACAQ&sid"
               "=28deaec43840af3789c593babab79aa1&lang=en-us&sb_price_type="
               "total&soz=1&lang_click=other;cdl=ru;lang_changed=1")
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "myDynamicElement"))
        )
    finally:
        driver.quit()


def test_functonality():
    # driver.find_element_by_xpath('//*[@id="xp__guests__toggle"]').click()
    driver.find_element_by_id("xp__guests__toggle").click()
    time.sleep(3)

    # double click on button CHILDREN
    CHILD_NUMBER = driver.find_element_by_xpath('//button[@aria-label="Increase number of Children"]')
    actions = ActionChains(driver)
    actions.double_click(CHILD_NUMBER).perform()  # double click on button
    time.sleep(2)
    #  click on age selection_1
    time.sleep(2)
    DATA_GROUP_CHILD_AGE = driver.find_element_by_xpath("//select[@aria-label='Child 1 age']") \
        .click()  # click on age selection
    CHILD_AGE_SELECTION = driver.find_element_by_xpath('//select[@aria-label="Child 1 age"]//'
                                                       'option[@value="10"][normalize-space()="10 years old"]').click()
    time.sleep(2)
    #  click on age selection_2
    DATA_GROUP_CHILD_AGE_2 = driver.find_element_by_xpath("//select[@aria-label='Child 2 age']") \
        .click()  # click on age selection
    CHILD_AGE_SELECTION_1 = driver.find_element_by_xpath('//select[@aria-label="Child 2 age"]//'
                                                         'option[@value="5"][normalize-space()="5 years old"]').click()
    EMPTY_FIELD = driver.find_element_by_xpath('//div[@class="xpi__searchbox '
                                 'js-ds-layout-events-search-form"]').click()  # click on empty field
# def test_down():
#     driver.close()
#     driver.quit()
#     print("Test Complete")
