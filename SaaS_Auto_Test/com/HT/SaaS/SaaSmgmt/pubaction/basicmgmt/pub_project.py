#coding=utf-8
'''
Created on 2017/8/2

@author: "luozhongjian"
'''

from time import sleep
from selenium.webdriver.common.action_chains import ActionChains



class Project:

    driver = ""
    dict_Project_info =  []
   
     
    def __init__(self, driver, dict_Project_info):

        self.driver =driver
        self.dict_Project_info = dict_Project_info


    def add_project(self):
        '''新增项目'''
        
        driver = self.driver
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@class='iframe']"))
        sleep(2)
        
        #点击新增按钮
        driver.find_element_by_xpath("//*[@id='mainGrid']/div[3]/div[1]/div[3]").click()
        sleep(3)
        
        #选择企业
        driver.find_element_by_xpath("//*[@id='enterpriseSelect']").click()
        sleep(1)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("//*[@id='_DialogFrame_0fk']"))
        sleep(1)
        driver.find_element_by_xpath("//*[@id='polluteName']").send_keys(self.dict_Project_info[u'企业名称'])
        sleep(1)
        driver.find_element_by_xpath("//*[@id='publicCon']/div[2]/button[1]").click()
        sleep(1)
        driver.find_element_by_xpath("//*[@id='dataBasic|2|r1001|c102']/div").click()
        
        driver.switch_to_default_content()
        driver.find_element_by_xpath("//*[@id='_ButtonOK_0fk']").click()
        sleep(1)
        
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@class='iframe']"))
        #项目名称
        driver.find_element_by_xpath("//th[contains(text(), '项目名称')]/following::td[1]/input").send_keys(self.dict_Project_info[u'项目名称'])
        sleep(1)
    
        #项目地址-行政区划
        address = self.dict_Project_info[u"项目地址"].split('-')
        #省
        driver.find_element_by_xpath("//th[contains(text(), '项目地址')]/following::td/input").click()
        sleep(1)
        driver.find_element_by_xpath("//li[text()='%s']" % (address[0])).click()
        sleep(1)
        #市
        driver.find_element_by_xpath("//*[@id='myFormId']/div[1]/table/tbody/tr[5]/th[1]/following::td/input").click()
        sleep(1)
        ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id='myFormId']/div[1]/table/tbody/tr[5]/td[1]/div//li[text()='%s']" % (address[1]))).perform()
        sleep(1)
        driver.find_element_by_xpath("//li[text()='%s']" % (address[1])).click()
        sleep(1)
        #区
        driver.find_element_by_xpath("//*[@id='myFormId']/div[1]/table/tbody/tr[6]/th[1]/following::td/input").click()
        sleep(1)
        ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id='myFormId']/div[1]/table/tbody/tr[6]/td[1]/div//li[text()='%s']" % (address[2]))).perform()
        sleep(1)
        driver.find_element_by_xpath("//li[text()='%s']" % (address[2])).click()
        sleep(1)
        #街道
        driver.find_element_by_xpath("//*[@id='myFormId']/div[1]/table/tbody/tr[7]/th[1]/following::td/input").click()
        sleep(1)
        ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id='myFormId']/div[1]/table/tbody/tr[7]/td[1]/div//li[text()='%s']" % (address[3]))).perform()
        sleep(2)
        driver.find_element_by_xpath("//li[text()='%s']" % (address[3])).click()
        sleep(1)
        
        #村
        driver.find_element_by_xpath("//*[@id='myFormId']/div[1]/table/tbody/tr[8]/th[1]/following::td/input").click()
        sleep(1)
        ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id='myFormId']/div[1]/table/tbody/tr[8]/td[1]/div//li[text()='%s']" % (address[4]))).perform()
        sleep(2)
        driver.find_element_by_xpath("//li[text()='%s']" % (address[4])).click()
        sleep(1)
        
        #详细地址
        driver.find_element_by_xpath("//th[contains(text(), '详细地址')]/following::td[1]/input").send_keys(self.dict_Project_info[u'详细地址'])

        #行业类别    
        driver.find_element_by_xpath("//th[contains(text(), '行业类别')]/following::td/div").click()
        driver.find_element_by_xpath("//a//span[text()='%s']" % (self.dict_Project_info[u"行业类别"])).click()
        sleep(1)
            
        #分类管理名录
        if not self.dict_Project_info[u'分类管理名录'] == "":     
            driver.find_element_by_xpath("//th[contains(text(), '分类管理名录')]/following::td/div").click()
            driver.find_element_by_xpath("//a//span[text()='%s']" % (self.dict_Project_info[u"分类管理名录"])).click()
            sleep(1)   

        #建设性质
        if not self.dict_Project_info[u"建设性质"] == "":
            driver.find_element_by_xpath("//th[contains(text(), '建设性质')]/following::td[1]//input").click()
            sleep(1)
            driver.find_element_by_xpath("//li[text()='%s']" % (self.dict_Project_info[u"建设性质"])).click()
            sleep(1)
             
            
        #预计开工时间
        driver.find_element_by_xpath("//th[contains(text(), '预计开工时间')]/following::td/input").send_keys(self.dict_Project_info[u'预计开工时间'])

        #预计投产时间
        driver.find_element_by_xpath("//th[contains(text(), '预计投产时间')]/following::td/input").send_keys(self.dict_Project_info[u'预计投产时间'])
   
        #是否是工地  
        driver.find_element_by_xpath("//th[contains(text(), '是否是工地')]/following::td[1]//input").send_keys(self.dict_Project_info[u"是否是工地"])
        sleep(1)
        
        #是否辐射项目 
        driver.find_element_by_xpath("//th[contains(text(), '是否辐射项目')]/following::td[1]//input").send_keys(self.dict_Project_info[u"是否辐射项目"])
        sleep(1)

        #状态
        driver.find_element_by_xpath("//th[contains(text(), '状态')]/following::td[1]//input").click()
        sleep(1)
        driver.find_element_by_xpath("//li[text()='%s']" % (self.dict_Project_info[u"状态"])).click()
        sleep(1)

        #提交按钮
        driver.find_element_by_xpath("//button[text()=' 提交']").click()
        sleep(2) 
        driver.switch_to_default_content()
        sleep(2)
        
        if driver.find_element_by_xpath("//*[@id='Message_undefined']").text ==u'新增建设项目成功！':   
            sleep(1)
            driver.find_element_by_xpath("//*[@id='_ButtonCancel_0fk']").click()
            return True
        else:
            return False
            
            
        
        
        
        
        
        
    