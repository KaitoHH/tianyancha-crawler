from selenium import webdriver
import csv
import io
import re
import utils


def getCompanyInfo(url):
    print(url)
    browser.get(url)
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
            print('can not find specific element, fix it and press enter...', end='')
            input()
            retry = True
    try:
        element = browser.find_element_by_xpath(
            '//*[@id="_container_holder"]/div/table/tbody')
    except:
        return None
    spt = element.text.split('\n')
    groups = [[company_name] + spt[x:x + 1] + spt[x + 2:x + 4]
              for x in range(0, len(spt), 4)]
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
            with open('company_detail/company_{:02d}.txt'.format(i), 'a', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, delimiter='|')
                writer.writerows(result)
