#coding=utf-8
'''
Created on 2017/8/2

@author: "luozhongjian"

建设项目--申报流程
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
from com.HT.SaaS.SaaSmgmt.pubaction.amsflow.pub_approval import approval
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
    sheet = excel.getSheetByName(book, u"建设项目流程")

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
    access_module(driver, u"建设项目审批", u"行政办公", u"报件登记")
     
    #新增报件
    approvalrep = approval(driver, testDataDic)
    addApprovalRes = approvalrep.Newspaper_registration()
    if addApprovalRes:
        reporter.reportEvent("Passed", u"新增报件", u"新增成功！")
    else:
        reporter.reportEvent("Failed", u"新增报件", u"新增失败！")
             


def sys_check(): 
    '''检查点'''
    
    global reporter, driver, testDataDic,dict_approval_info
    
    access_module(driver, u"建设项目审批", u"行政办公", u"报件查询")
    
    driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@class='iframe']"))
    
    dict_approval_info = testDataDic
    #选择报件状态
    newstype = dict_approval_info[u"报件状态"].split('-')
    driver.find_element_by_xpath("//th[contains(text(), '报件状态')]/following::td/input").click()
    sleep(1)
    driver.find_element_by_xpath("//li[text()='%s']" % (newstype[0])).click()
    sleep(1)
    
    #点击更多
    driver.find_element_by_xpath("//span[text()='更多>']").click()
    #输入查询条件-项目名称
    driver.find_element_by_xpath("//*[@id='projectName']").send_keys(testDataDic[u'项目名称'])
    sleep(2)
    #点击查询按钮
    driver.find_element_by_xpath("//button[text()='查询']").click()
    sleep(2)
    try:
        if driver.find_element_by_xpath("//*[@id='dataBasic|2|r1001|c113']/div").text == newstype[0]:
        
            reporter.reportEvent("Passed", u"报件状态一致", newstype[0] )   
        else:
            reporter.reportEvent("Failed", u"报件状态不一致", newstype[0] ) 
    except:
        reporter.reportEvent("Failed", u"查询报件", u"查询结果为空") 
       
    #点击查看按钮   
    driver.find_element_by_xpath("//*[@id='dataBasic|2|r1001|c104']/div/a").click()    
    sleep(1)
    
    #获取句柄
    nowhandle = driver.current_window_handle
    allhandles = driver.window_handles
    for handle in allhandles:
        if handle != nowhandle: 
            driver.switch_to_window(handle)
            
    driver.maximize_window()
            
    sleep(2)
    driver.switch_to_default_content()
    
    driver.find_element_by_xpath("//td[text()='报件登记']").click()
    sleep(2)
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@id='page_tab1_index1']"))  
    
    #获取查看界面的th,td
    fldName = driver.find_elements_by_xpath("//div[@class='form-group']//th") 
    fldValue = driver.find_elements_by_xpath("//div[@class='form-group']//td")
    
    approvalInfoDic = {}
    i = 0
    
    for i in range(len(fldName)):

        approvalInfoDic[fldName[i].text.strip(u'：')] = fldValue[i].text

    expectedResult = testDataDic
    del expectedResult[u'处理人']
    del expectedResult[u'材料上传']
    del expectedResult[u'报件状态']
    del expectedResult[u'批文模板']
    
    
    for key, value in expectedResult.items():
        if approvalInfoDic[key] == value:
            
            reporter.reportEvent("Passed", "Check_" + key + " - " + value, approvalInfoDic[key])
        else:
            reporter.reportEvent("Failed", "Check_" + key + " - " + value, approvalInfoDic[key])
             
     
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