#coding=utf-8
'''
Created on 2017年8月21日

@author: "luozhongjian"
'''

import HTMLTestRunner
import unittest
from com.HT.SaaS.SaaSmgmt.scripts.basicmgmt import add_ams_enterprise
from com.HT.SaaS.SaaSmgmt.scripts.basicmgmt import add_report_project


class Test_basicmgmt(unittest.TestCase):
    u'''新增企业和项目'''

    def test_add_ams_enterprise(self):
        u'''新增企业'''
        add_ams_enterprise.run()
        
    def test_add_report_project(self):
        u'''新增项目'''
        add_report_project.run()

  

def get_suite(): 
           
    basicmgmt_suite = unittest.TestSuite([Test_basicmgmt("test_add_ams_enterprise"), Test_basicmgmt("test_add_report_project")])
    return basicmgmt_suite

if __name__ == "__main__":
    
    basicmgmt_suite = unittest.TestSuite([Test_basicmgmt("test_add_ams_enterprise"), Test_basicmgmt("test_add_report_project")])
    report = open("ams_basicmgmt_report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream = report, title = "Automation Test Report", description = "SaaS")
    runner.run(basicmgmt_suite)
    report.close()
                
