from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from PIL import Image, ImageEnhance

URL = "https://passport.bilibili.com/login"
URL2 = "https://www.autohome.com.cn"

#截取页面
def get_page_source(url):
    browser = webdriver.Chrome()
    browser.get(url)
    sleep(5)
    page_source = browser.page_source
    print(page_source)
    browser.get_screenshot_as_file("test.png")
    browser.close()

    return page_source

#PIL裁切截图
def crop_image():
    driver = webdriver.Chrome()
    # driver.maximize_window()
    
    driver.get("https://www.autohome.com.cn")
    driver.save_screenshot('capture.png')    #截取全屏
    ele = driver.find_element_by_id('s4612')
    #获取元素位置信息
    left = ele.location['x']
    top = ele.location['y']
    right = left + ele.size['width']
    bottom = top + ele.size['height']
    im = Image.open('capture.png')
    im = im.crop((left, top, right, bottom))    #元素裁剪
    im.save('ele_capture.png')    #元素截图
    
    driver.quit()


#元素截图 似乎是错的
def get_screenshot_as_crop(url):
    browser = webdriver.Chrome()
    browser.get(url)
    sleep(2)
    # x = '//*[@id="login-app"]/div/div[2]/div[3]/div[1]/div/div[1]/div/div[1]'
    # i = 'qrcode-img'
    ele = browser.find_element_by_id('internationalHeader')
    print("element: ",ele)
    ele.screenshot("code.png")
    browser.close()

if __name__ == '__main__':
    crop_image()