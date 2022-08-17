#coding=utf-8

from time import sleep
from selenium.webdriver.common.action_chains import ActionChains




class Enterprise:

    driver = ""
    dict_enterprise_info =  []
   
     
    def __init__(self, driver, dict_enterprise_info):

        self.driver =driver
        self.dict_enterprise_info = dict_enterprise_info


    def add_enterprise(self):
        """新增模板"""
        
        driver = self.driver
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@class='iframe']"))
        sleep(2)
        
        #点击新增按钮
        driver.find_element_by_xpath("//div[@class='l-icon icon_add']").click()
        sleep(3)
        
        #企业名称
        driver.find_element_by_xpath("//th[contains(text(), '企业名称')]/following::td[1]/input").send_keys(self.dict_enterprise_info[u'企业名称'])
        sleep(1)
        
        #企业地址-行政区划
        address = self.dict_enterprise_info[u"企业地址"].split('-')
        
        driver.find_element_by_xpath("//th[contains(text(), '企业地址')]/following::td/input").click()
        sleep(1)
        driver.find_element_by_xpath("//li[text()='%s']" % (address[0])).click()
        sleep(1)
        
        driver.find_element_by_xpath("//*[@id='myFormId']/div[1]/table/tbody/tr[4]/th[1]/following::td/input").click()
        ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id='myFormId']/div[1]/table/tbody/tr[4]/td[1]/div//li[text()='%s']" % (address[1]))).perform()
        sleep(1)
        driver.find_element_by_xpath("//li[text()='%s']" % (address[1])).click()
        sleep(1)
        
        driver.find_element_by_xpath("//*[@id='myFormId']/div[1]/table/tbody/tr[5]/th[1]/following::td/input").click()
        ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id='myFormId']/div[1]/table/tbody/tr[5]/td[1]/div//li[text()='%s']" % (address[2]))).perform()
        sleep(1)
        driver.find_element_by_xpath("//li[text()='%s']" % (address[2])).click()
        sleep(1)
        
        driver.find_element_by_xpath("//*[@id='myFormId']/div[1]/table/tbody/tr[6]/th[1]/following::td/input").click()
        ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id='myFormId']/div[1]/table/tbody/tr[6]/td[1]/div//li[text()='%s']" % (address[3]))).perform()
        sleep(2)
        driver.find_element_by_xpath("//li[text()='%s']" % (address[3])).click()
        sleep(1)
        
        driver.find_element_by_xpath("//*[@id='myFormId']/div[1]/table/tbody/tr[7]/th[1]/following::td/input").click()
        ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id='myFormId']/div[1]/table/tbody/tr[7]/td[1]/div//li[text()='%s']" % (address[4]))).perform()
        sleep(2)
        driver.find_element_by_xpath("//li[text()='%s']" % (address[4])).click()
        sleep(1)
        
        #详细地址
        driver.find_element_by_xpath("//th[contains(text(), '详细地址')]/following::td[1]/input").send_keys(self.dict_enterprise_info[u'详细地址'])

        #企业性质
        if not self.dict_enterprise_info[u"企业性质"] == "":
            driver.find_element_by_xpath("//th[contains(text(), '企业性质')]/following::td[1]//input").click()
            sleep(1)
            driver.find_element_by_xpath("//li[text()='%s']" % (self.dict_enterprise_info[u"企业性质"])).click()
            sleep(1)
            
        #企业类型
        if not self.dict_enterprise_info[u"企业类型"] == "":
            driver.find_element_by_xpath("//th[contains(text(), '企业类型')]/following::td[1]//input").click()
            sleep(1)
            driver.find_element_by_xpath("//li[text()='%s']" % (self.dict_enterprise_info[u"企业类型"])).click()
            sleep(1)
        
        #行业类别
        Industry = self.dict_enterprise_info[u"行业类别"].split('-')
        driver.find_element_by_xpath("//th[contains(text(), '行业类别')]/following::td/div").click()
        sleep(1)
        driver.find_element_by_xpath("//a//span[text()='%s']" % (Industry[0])).click()
        sleep(1)
        driver.find_element_by_xpath("//a//span[text()='%s']" % (Industry[1])).click()
        sleep(1)
        driver.find_element_by_xpath("//a//span[text()='%s']" % (Industry[2])).click()
        sleep(1)
        driver.find_element_by_xpath("//a//span[text()='%s']" % (Industry[3])).click()
        sleep(1)
        
        #企业状态
        if not self.dict_enterprise_info[u'企业状态'] == "":     
            driver.find_element_by_xpath("//th[contains(text(), '企业状态')]/following::td[1]//input").click()
            sleep(1)
            driver.find_element_by_xpath("//li[text()='%s']" % (self.dict_enterprise_info[u"企业状态"])).click()
            sleep(1)

        
        #提交按钮
        driver.find_element_by_xpath("//button[text()='保存']").click()
        sleep(2) 
        driver.switch_to_default_content()
        sleep(1)
        
        if driver.find_element_by_xpath("//*[@id='Message_undefined']").text ==u'添加成功！':   
            sleep(1)
            driver.find_element_by_xpath("//*[@id='_ButtonCancel_0fk']").click()
            return True
        else:
            return False
            
            
        
        
        
        
        
        
    