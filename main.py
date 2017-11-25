from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import csv
import utils
import time
import captcha


def getCompanyInfo(url):
    print(url)
    browser.get(url)
    if not captcha.get_captcha(browser):
        print('fatal error! program paused...')
        input()
    retry = False
    while True:
        try:
            company_name = browser.find_element_by_xpath(
                '//*[@id="company_web_top"]/div[2]/div[2]/div/span[1]').text
            break
        except:
            if retry:
                print('still failed to find element, skip current page...')
                return None
            print('can not find specific element, retry...', end='')
            # input()
            retry = True
    groups = []
    next_page = 2
    count = 0
    while True:
        count += 1
        try:
            name = browser.find_element_by_xpath(
                '//*[@id="_container_holder"]/div/table/tbody/tr[{:d}]/td[1]/a'.
                format(count)).text
            precent = browser.find_element_by_xpath(
                '//*[@id="_container_holder"]/div/table/tbody/tr[{:d}]/td[2]/div/div/span'.
                format(count)).text
            amount = browser.find_element_by_xpath(
                '//*[@id="_container_holder"]/div/table/tbody/tr[{:d}]/td[3]/div/span[1]'.
                format(count)).text
            groups.append([company_name, name, precent, amount])
        except:
            try:
                target = '//*[@id="_container_holder"]/div/div/ul/li[{:d}]/a'.format(
                    next_page + 1)
                element = browser.find_element_by_xpath(target)
                next_page = int(element.text) + 1

                # scroll down
                actions = ActionChains(browser)
                actions.move_to_element(element).send_keys(
                    Keys.DOWN).send_keys(Keys.DOWN).pause(1).perform()
                element.click()

                time.sleep(1)
                count = 0
            except:
                return groups


browser = webdriver.Chrome()
browser.maximize_window()
utils.auto_login(browser)
start_oc = 1
for i in range(start_oc, 97):
    f = open('company_list/company_{:02d}.txt'.format(i), 'r')
    for line in f.readlines():
        result = getCompanyInfo(line.strip())
        if result:
            with open(
                    'company_detail/company_{:02d}.txt'.format(i),
                    'a',
                    encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, delimiter='|')
                writer.writerows(result)
