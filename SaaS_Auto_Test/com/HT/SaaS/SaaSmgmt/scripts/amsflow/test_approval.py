#coding=utf-8
'''
Created on 2017年8月21日

@author: "luozhongjian"
'''

import HTMLTestRunner
import unittest, doctest
from com.HT.SaaS.SaaSmgmt.scripts.amsflow import approval_newspaper
from com.HT.SaaS.SaaSmgmt.scripts.amsflow import approval_investigate
from com.HT.SaaS.SaaSmgmt.scripts.amsflow import approval_to_examine
from com.HT.SaaS.SaaSmgmt.scripts.amsflow import approval_examination
from com.HT.SaaS.SaaSmgmt.scripts.amsflow import approval_document

class Test_approval(unittest.TestCase):
    u'''建设项目流程'''

    def test_approval_newspaper(self):
        u'''报件登记'''
        approval_newspaper.run()
        
    def test_approval_investigate(self):
        u'''审查'''
        approval_investigate.run()
        
    def test_approval_to_examine(self):
        u'''审核'''
        approval_to_examine.run() 
        
    def test_approval_examination(self):
        u'''审批'''
        approval_examination.run()  
        
    def test_approval_document(self):
        u'''制文'''
        approval_document.run()
        
        
    

def get_suite(): 
           
    approval_suite = unittest.TestSuite([Test_approval("test_approval_newspaper"), 
                                         Test_approval("test_approval_investigate"), 
                                         Test_approval("test_approval_to_examine"),
                                         Test_approval("test_approval_examination"),
                                         Test_approval("test_approval_document")])
    
#     approval_suite = unittest.TestSuite([Test_approval("test_approval_newspaper")])
    return approval_suite







if __name__ == "__main__":
    
    #approval_suite = unittest.TestSuite([Test_approval("test_approval_newspaper")])
    approval_suite = unittest.TestSuite([Test_approval("test_approval_newspaper"), 
                                          Test_approval("test_approval_investigate"), 
                                          Test_approval("test_approval_to_examine"),
                                          Test_approval("test_approval_examination"),
                                          Test_approval("test_approval_document")])
     
    report = open("D:/auto_test_component/automation_test_report_AMS.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream = report, title = "Automation Test Report", description = "SaaS")
    result= runner.run(approval_suite)
    report.close()
     
     

    

    
    
                
