#coding=utf-8
'''
Created on 2017/8/2

@author: "luozhongjian"

新增企业
'''

import inspect
import os
from string import replace
import sys
from time import sleep

from com.HT.SaaS.SaaSmgmt import report, testdata
from com.HT.SaaS.SaaSmgmt.library.excelstand import ExcelApp
from com.HT.SaaS.SaaSmgmt.pubaction.sysaccess.loginsys import login
from com.HT.SaaS.SaaSmgmt.pubaction.sysaccess.syspage import access_module
from com.HT.SaaS.SaaSmgmt.pubaction.basicmgmt.pub_enterprise import Enterprise
from com.HT.SaaS.SaaSmgmt.report.reporter import Reporter



#全局变量
driver = ""
reporter = ""
testDataDic = {}



def load_data():
    '''读取数据'''

    global testDataDic
    #读取Excel的数据
    excel = ExcelApp(replace(inspect.getfile(testdata).strip("__init__.pyc"), "\\", "/") + "/InputData.xls", [])
    book = excel.openExcel("r")
    sheet = excel.getSheetByName(book, u"企业管理")

    i = 0
    testDataDic = {}
    while not excel.getCellData(sheet, 1, i) == "":

        testDataDic[excel.getCellData(sheet, 1, i)] = excel.getCellData(sheet, 2, i)
        i = i + 1

def create_report():
    '''生成报告'''
    
    
    global reporter
    rptName = replace(inspect.getfile(report).strip("__init__.pyc"), "\\", "/") + "rpt_" + os.path.basename(__file__).strip(".pyc") + ".xls"
    rptShtName = "result"
    reporter = Reporter(rptName, rptShtName)   


def do_action(): 
    '''执行脚本'''
    
    
    global reporter, driver, testDataDic
    #登录
    loginres = login()
    driver = loginres["driver"]
    if loginres['login'] == True:
        reporter.reportEvent("Passed", u"登录系统", loginres['login'])
        
    else:
        reporter.reportEvent("Failed", u"登录系统", loginres['login'])
        
        sys.exit()
    
    #定位模块
    access_module(driver, u"审批配置", u"基础管理", u"企业管理")
     
#     #新增企业
    Enterpriserep = Enterprise(driver, testDataDic)
    addEnterpriserRes = Enterpriserep.add_enterprise()
    if addEnterpriserRes:
        reporter.reportEvent("Passed", u"新增企业", u"新增成功！")
    else:
        reporter.reportEvent("Failed", u"新增企业", u"新增失败！")
      


def sys_check(): 
    '''检查点'''
    
    global reporter, driver, testDataDic
     
    driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@class='iframe']"))
    
    #输入查询条件-企业名称
    driver.find_element_by_xpath("//*[@id='enterpriseName']").send_keys(testDataDic[u'企业名称'])
    sleep(2)
    
    #点击查询按钮
    driver.find_element_by_xpath("//*[@id='searc_button']").click()
    sleep(2)
    
    #点击查看按钮
    driver.find_element_by_xpath("//*[@id='dataBasic|2|r1001|c108']/div/div/span[1]").click()
    sleep(1)
     
    fldName = driver.find_elements_by_xpath("//table[@class='form-table']//th")
    fldValue = driver.find_elements_by_xpath("//table[@class='form-table']//td")
    enterpriseInfoDic = {}
    i = 0
    
    for i in range(len(fldName)):

        enterpriseInfoDic[fldName[i].text.strip(u"：")] = fldValue[i].text

    expectedResult = testDataDic
    del expectedResult[u'企业地址']
    del expectedResult[u'行业类别']
       
    for key, value in expectedResult.items():
        if enterpriseInfoDic[key] == value:
            
            reporter.reportEvent("Passed", "Check_" + key + " - " + value, enterpriseInfoDic[key])
        else:
            reporter.reportEvent("Failed", "Check_" + key + " - " + value, enterpriseInfoDic[key])
             
     
    
    driver.switch_to_default_content()

    driver.quit()
  

def run():
    '''执行方法'''
    create_report()

    load_data()

    do_action()

    sys_check()
        
    
if __name__ == '__main__':
    run()
    