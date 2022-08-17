from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 解决浏览器弹出2个页面的问题
# DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True


def login():
    '''登录'''

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

    # # 谷歌浏览器启动
    # chromeDriver = "D:\software\Python38\chromedriver.exe"
    # os.environ["webdriver.chrome.driver"] = chromeDriver
    # driver = webdriver.Chrome(chromeDriver)
    driver.get('http://192.168.0.58:3100/#/login?redirect=/login/core')
    driver.maximize_window()
    driver.implicitly_wait(8)
    driver.find_element(By.ID, "form_item_account").clear()
    driver.find_element(By.ID, "form_item_account").send_keys('admin')
    driver.find_element(By.ID, "form_item_password").clear()
    driver.find_element(By.ID, "form_item_password").send_keys('admin123456')
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[text()='立即登录']").click()

    time.sleep(5)


if __name__ == '__main__':

    login()

