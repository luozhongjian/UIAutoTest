#coding=utf-8
'''
Created on 2017年8月21日

@author: "luozhongjian"
'''

import HTMLTestRunner
import unittest
from com.HT.SaaS.SaaSmgmt.scripts.licenseflow import license_newspaper
from com.HT.SaaS.SaaSmgmt.scripts.licenseflow import license_investigate
from com.HT.SaaS.SaaSmgmt.scripts.licenseflow import license_to_examine
from com.HT.SaaS.SaaSmgmt.scripts.licenseflow import license_examination
from com.HT.SaaS.SaaSmgmt.scripts.licenseflow import license_document


class Test_license(unittest.TestCase):
    u'''许可证流程'''

    def test_license_newspaper(self):
        u'''新增许可证'''
        license_newspaper.run()
        
    def test_license_investigate(self):
        u'''制作许可证'''
        license_investigate.run()
        
    def test_license_to_examine(self):
        u'''审核许可证'''
        license_to_examine.run() 
        
    def test_license_examination(self):
        u'''审批许可证'''
        license_examination.run()  
        
    def test_license_document(self):
        u'''制文许可证'''
        license_document.run()
        
        
  

def get_suite(): 
           
    license_suite = unittest.TestSuite([Test_license("test_license_newspaper"),
                                        Test_license("test_license_investigate"),
                                        Test_license("test_license_to_examine"),
                                        Test_license("test_license_examination"),
                                        Test_license("test_license_document")])

    return license_suite


if __name__ == "__main__":

    license_suite = unittest.TestSuite([Test_license("test_license_newspaper"), 
                                        Test_license("test_license_investigate"), 
                                        Test_license("test_license_to_examine"),
                                        Test_license("test_license_examination"),
                                        Test_license("test_license_document")])
 
    
    report = open("D:/automation_test_report_AMS.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream = report, title = "Automation Test Report", description = "SaaS")
    runner.run(license_suite)

    report.close()
     
