from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
import time
import base64
import json
import image
import api


def click(browser, element, x, y):
    actions = ActionChains(browser)
    actions.move_to_element_with_offset(
        element, x, y).click_and_hold().release().perform()


def get_captcha(browser):
    fail_count = -1
    while True:
        time.sleep(1)
        try:
            imgA = browser.find_element_by_xpath('//*[@id="targetImgie"]')
            fail_count += 1
        except:
            return True
        print('captcha found!')
        imgB = browser.find_element_by_xpath('//*[@id="bgImgie"]')
        urllib.request.urlretrieve(imgA.get_attribute('src'), 'A.png')
        urllib.request.urlretrieve(imgB.get_attribute('src'), 'B.png')
        image.merge_captcha()
        print('sending request...')
        result = api.post()
        result = json.loads(result)
        print(result)
        pos = result['data']['val'].split('|')
        for point in pos:
            x, y = point.split(',')
            click(browser, imgB, int(x), int(y))
            time.sleep(0.3)
        submit = browser.find_element_by_xpath('//*[@id="submitie"]')
        submit.click()
        if fail_count >= 10:
            return False
