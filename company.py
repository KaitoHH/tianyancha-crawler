from selenium import webdriver
import utils
browser = webdriver.Chrome()
browser.maximize_window()
utils.auto_login(browser)
start_oc = 1
for i in range(start_oc, 97):
    file = open('company_list/company_' + '{:02d}'.format(i) + '.txt', 'w')
    for j in range(1, 6):
        url = 'https://www.tianyancha.com/search/oc{:02d}/p{:d}'.format(i, j)
        print(url)
        browser.get(url)
        flag = True
        while True:
            elements = browser.find_elements_by_class_name('search_right_item')
            for element in elements:
                a = element.find_element_by_tag_name('a')
                file.write(a.get_attribute("href") + '\n')
            if not elements:
                if flag:
                    print('can not find any company url, press enter to move on...', end='')
                    input()
                    flag = False
                else:
                    print('still can not find any url, skip current url...')
                    break
            else:
                break
    file.close()
