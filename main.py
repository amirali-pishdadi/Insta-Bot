import json
from os.path import exists as ope
import time
from selenium import webdriver
from xpath import get_xpath
from browser import Browser, _write
from until import not_now

username = "Your username"
password = "Your password"
main_url = "https://www.instagram.com/"


def check_login(browser):
    try:
        browser.find_element_by_xpath(get_xpath('Home', 'profile'))
        return True
    except:
        return False


if __name__ == '__main__':
    mybr = Browser('geckodriver.exe')
    mybr.Change_Url(main_url)

    if ope(f'{username}.pkl'):
        mybr.load_cookies(username)
        not_now(mybr.driver, get_xpath('Home', 'sava_not'))
        # time.sleep(2)
        # not_now(mybr.driver, get_xpath('Home', 'sava_not'))
    else:
        el_un = mybr.driver.find_element_by_xpath(get_xpath('Login', 'username'))
        el_pw = mybr.driver.find_element_by_xpath(get_xpath('Login', 'password'))
        _write(username, el_un)
        _write(password, el_pw)
        mybr.driver.find_element_by_xpath(get_xpath('Login', 'submit')).click()
        time.sleep(0.5)
        not_now(mybr.driver, get_xpath('Home', 'sava_not'))
        time.sleep(2)
        not_now(mybr.driver,get_xpath('Home', 'sava_not'))
        if check_login(mybr.driver):
            mybr.sava_cookie(username)
    # -----------
    Data = mybr.driver.execute_script('return window._sharedData')
    print(Data)
    # json.dump(Data)
