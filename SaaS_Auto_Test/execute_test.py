#coding=utf-8
'''
Created on 2017/8/27

@author: luozhongjian
'''
import HTMLTestRunner
import glob
import os
import unittest

from com.HT.SaaS.SaaSmgmt.report.reporter import Reporter
from com.HT.SaaS.SaaSmgmt.scripts.amsflow import test_approval
from com.HT.SaaS.SaaSmgmt.scripts.basicmgmt import test_basicmgmt
from com.HT.SaaS.SaaSmgmt.scripts.licenseflow import test_license
import emailReport

import sys
reload(sys)
sys.setdefaultencoding("utf-8")



def totalsuite_test():
    
    report = open("D:/auto_test_component/automation_test_report_AMS.html", "wb")
     
    totalsuite = unittest.TestSuite()

    #totalsuite.addTests(test_basicmgmt.get_suite())
    totalsuite.addTests(test_approval.get_suite())
    totalsuite.addTests(test_license.get_suite())

    '''执行之前清空所有报告'''
    for rpt in glob.glob(os.path.join(os.getcwd().replace("\\","/") + "/com/HT/SaaS/SaaSmgmt/report/", "*.xls")):
        os.remove(rpt)
    if os.path.exists("report_summary.xls"):
        os.remove("report_summary.xls")
        
    '''触发执行'''
    runner = HTMLTestRunner.HTMLTestRunner(stream = report, title = "Automation Test Report", description = "SEPV3 - SaaS")
    result = runner.run(totalsuite)

    
#     '''获取unittest报告信息'''
    runner.getReportAttributes(result)

    
    dicReportInfo = {}
    for item in runner.getReportAttributes(result):
        dicReportInfo[item[0]] = item[1]
        
    
    f = open('D:/auto_test_component/ams_log.txt', 'w')
    for key,value in dicReportInfo.items():
        f.write(key+':'+value)
        f.write("\n")
    f.close()
    
    
    '''运行excel报告汇总'''
    rpt = Reporter("ReportSummary.xls", "TestSummary")
    rpt.reportSummary(os.getcwd().replace("\\","/") + "/com/HT/SaaS/SaaSmgmt/report/")
    #emailReport.send_report()
    
    
if __name__ == '__main__':
    totalsuite_test()
    
   
    