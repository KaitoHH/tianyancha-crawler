from selenium import webdriver
import io
import re
import utils


def getCompanyInfo(url):
    print(url)
    browser.get(url)
    company_name = browser.find_element_by_xpath(
        '//*[@id="company_web_top"]/div[2]/div[2]/div/span[1]')
    print(company_name.text)
    element = browser.find_element_by_xpath(
        '//*[@id="_container_holder"]/div/table/tbody')
    spt = element.text.split('\n')
    groups = [spt[x:x + 1] + spt[x + 2:x + 4] for x in range(0, len(spt), 4)]
    print(*groups, sep='\n')


f = open('company_list/company_01.txt', 'r')
browser = webdriver.Chrome()
browser.maximize_window()

utils.auto_login(browser)

for line in f.readlines():
    getCompanyInfo(line.strip())
    # with open('info.txt', 'a', encoding='utf-8') as file:
    #     file.write('\n'.join(result))
