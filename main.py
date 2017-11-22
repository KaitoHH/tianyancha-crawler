from selenium import webdriver
import io
import re


def getCompanyInfo(company_id):
    company_id = str(company_id)
    browser.get('https://www.tianyancha.com/company/' + company_id)
    element = browser.find_element_by_id('_container_holder')
    info = io.StringIO(element.text).readlines()[1:]
    result = []
    for x in range(len(info) // 4):
        temp = [company_id] + info[4 * x:4 * x + 3]
        r = re.findall(r'(.*?)\s*万', info[4 * x + 3])
        temp.append(r[0] if r else 'N/A')
        result.append('|'.join(temp))
    result = list(map(lambda x: re.sub(r'\n', '', x), result))
    return result


browser = webdriver.Chrome()
browser.maximize_window()
browser.set_window_position(-10000, 0)

company_id = 720901373
result = getCompanyInfo(company_id)

with open('info.txt', 'a', encoding='utf-8') as file:
    file.write('\n'.join(result))
