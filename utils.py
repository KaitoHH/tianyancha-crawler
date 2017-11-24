import time
import json

def wait_for_login(browser):
    browser.get('https://www.tianyancha.com/login')
    print('please login and press enter...', end='')
    input()


def auto_login(browser):
    browser.get('https://www.tianyancha.com/login')
    user = browser.find_element_by_xpath(
        '//*[@id="web-content"]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/input')
    pwd = browser.find_element_by_xpath(
        '//*[@id="web-content"]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[3]/input')
    with open('config.json') as f:
        config = json.load(f)
        user.send_keys(config['username'])
        pwd.send_keys(config['password'])
    browser.find_element_by_xpath(
        '//*[@id="web-content"]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[5]').click()
    time.sleep(1)
