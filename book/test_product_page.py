from lib2to3.pgen2 import driver

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class TestSiteFunct():
    def test_click_on_the_button(self, chrome_drv):
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="xp__guests__toggle"]').click() #  click on button
        BTN_CLICK = driver.find_element_by_xpath('//button[@aria-label="Increase number of Children"]')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.double_click(BTN_CLICK).perform()  # double click on button

    def test_click_on_the_selection_1(self):
        #  click on age selection_1
        time.sleep(2)
        DATA_GROUP_CHILD_AGE = driver.find_element_by_xpath("//select[@aria-label='Child 1 age']") \
            .click()  # click on age selection
        CHILD_AGE_SELECTION = driver.find_element_by_xpath('//select[@aria-label="Child 1 age"]//'
                                                           'option[@value="10"]'
                                                           '[normalize-space()="10 years old"]').click()
    def test_click_on_the_selection_1(self):
        time.sleep(2)
        #  click on age selection_2
        DATA_GROUP_CHILD_AGE_2 = driver.find_element_by_xpath("//select[@aria-label='Child 2 age']") \
            .click()  # click on age selection
        CHILD_AGE_SELECTION_1 = driver.find_element_by_xpath('//select[@aria-label="Child 2 age"]//'
                                                             'option[@value="5"]'
                                                             '[normalize-space()="5 years old"]').click()
        EMPTY_FIELD = driver.find_element_by_xpath('//div[@class="xpi__searchbox '
                                                   'js-ds-layout-events-search-form"]').click()  # click on empty field

