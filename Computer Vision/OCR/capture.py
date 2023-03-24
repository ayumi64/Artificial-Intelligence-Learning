from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time
import re

#sonic账号地址
APP_ID = '20545078'
API_KEY = 'qROAdLBMg7msxQgCB5FBwXIc'
SECRECT_KEY = '2KEtyNrmIstLt48hzMvnAXaNMQKg88a6'

driver = webdriver.Chrome()

# 利用aip进行识别
def identify_words(index=0):
    from aip import AipOcr
    client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)
    p = get_pic()
    with open(p, 'rb') as f:
        img = f.read()
    message = client.basicGeneral(img)
    res = message['words_result']
    print(res)
    print('识别结果为: %s' % res[0]['words'])

    res1 = res[index]['words']

    """去除多余空格"""
    strinfo = re.compile(' ')
    res2 = strinfo.sub('', str(res1))
    print(res2)

    return res2
    # if len(res) == 0:
    #     return '1'
    # else:
    #     return res[index]['words']

def get_pic():
    driver.get('https://pc.xiaoheiban.cn/login/')
    driver.find_element_by_css_selector('#app > div > div > div > div.footer-main > div > div:nth-child(3) > p').click()
    time.sleep(3)
    driver.find_element_by_xpath("//div[@class='captcha-img']").screenshot('capture_code.png')
    path = 'capture_code.png'
    return path

def input_key():
    c = identify_words()
    driver.find_element_by_css_selector("#app > div > div > div > div:nth-child(1) > div > input:nth-child(2)").send_keys('13166229623')
    driver.find_element_by_css_selector("#app > div > div > div > div:nth-child(1) > div > input:nth-child(3)").send_keys('56749154aA')
    driver.find_element_by_xpath("//input[@class='ant-input code-input']").send_keys(c)
    driver.find_element_by_css_selector("#app > div > div > div > div:nth-child(1) > div > button").click()

if __name__ == "__main__":
    # identify_words()
    input_key()