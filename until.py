from selenium import webdriver


def not_now(driver, element):
    button = driver.find_element_by_xpath(element)
    button.click()
