# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/26 09:12
@Auth ： 罗忠建

"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from com.HT.SaaS.SaaSmgmt.library.xmlstand import XmlApp
from selenium.webdriver.common.by import By



def login(username="", password=""):
    """登录"""

    xmlapp = XmlApp("access.xml")
    url = xmlapp.getNodesByTag("addr")[0].text
    
    if username == "" and password == "":
        
        username = xmlapp.getNodesByTag("username")[0].text
        password = xmlapp.getNodesByTag("password")[0].text


    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    chrome_options.add_argument('window-size=1920x1080')  # 指定浏览器分辨率
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    # chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    # chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    # chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # 手动指定本机电脑使用的浏览器位置
    # 创建一个driver,进行后面的请求页面等操作，executable_path指定本机中chromedriver.exe的位置
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:\software\Python38\chromedriver.exe")

    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(8)

    dicLoginRes = {}
    driver.find_element(By.ID, "form_item_account").clear()
    driver.find_element(By.ID, "form_item_account").send_keys(username)
    driver.find_element(By.ID, "form_item_password").clear()
    driver.find_element(By.ID, "form_item_password").send_keys(password)
    sleep(2)
    driver.find_element(By.XPATH, "//span[text()='立即登录']").click()
    
    sleep(3)
    title = driver.find_element(By.XPATH, "//img[@class='logo_img vben-header-user-dropdown__header']")
    if title.is_displayed():
        
        dicLoginRes["login"] = True
    else:
        dicLoginRes["login"] = False
        
    dicLoginRes["driver"] = driver
    print(dicLoginRes)

    return dicLoginRes

if __name__ == '__main__':
    login()

    