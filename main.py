from selenium import webdriver
import csv
import io
import re
import utils


def getCompanyInfo(url):
    print(url)
    browser.get(url)
    company_name = browser.find_element_by_xpath(
        '//*[@id="company_web_top"]/div[2]/div[2]/div/span[1]').text
    try:
        element = browser.find_element_by_xpath(
            '//*[@id="_container_holder"]/div/table/tbody')
    except:
        return
    spt = element.text.split('\n')
    groups = [[company_name] + spt[x:x + 1] + spt[x + 2:x + 4]
              for x in range(0, len(spt), 4)]
    with open('info.txt', 'a', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerows(groups)


f = open('company_list/company_01.txt', 'r')
browser = webdriver.Chrome()
browser.maximize_window()

utils.auto_login(browser)

for line in f.readlines():
    getCompanyInfo(line.strip())
