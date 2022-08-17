#coding=utf-8
'''
Created on 2017/8/4

@author: test
'''
import os
from string import replace

from com.HT.SaaS.SaaSmgmt.library.excelstand import ExcelApp


class Reporter:
    
    excel = ""
    book = ""
    sheet = ""
    counter = 1

    def __init__(self, sRptname, sSheetname):
        
        #------------------------------------------------------------------------------ judge if file exists first
        if os.path.isfile(sRptname):
            os.remove(sRptname)
        #------------------------------------------------------------------------------ new create report
        self.excel = ExcelApp(sRptname,[sSheetname])
        self.book = self.excel.openExcel("w")
        self.sheet = self.excel.getSheetByIndex(self.book, 0)
        self.excel.setCellData(self.sheet, 0, 0, u"结果状态", True, "yellow", "black", "on")
        self.excel.setCellData(self.sheet, 0, 1, u"步骤名称", True, "yellow", "black", "on")
        self.excel.setCellData(self.sheet, 0, 2, u"结果描述", True, "yellow", "black", "on")
        self.excel.setCellData(self.sheet, 0, 3, u"测试结果", True, "yellow", "black", "on")
        self.excel.setCellData(self.sheet, 1, 3, "Passed", True, "green", "white") 
        

    def reportEvent(self, sStatus, sStep, sDesciption):    
        
        if sStatus == "Passed":
            forecolor = "green"
                 
        elif sStatus == "Failed":
            forecolor = "red"
            #------------------------------------------------------------------------------ set final test result
            self.excel.setCellData(self.sheet, 1, 3, sStatus, True, "red", "white")
            
        self.excel.setCellData(self.sheet, self.counter, 0, sStatus, True, "white", forecolor)
        self.excel.setCellData(self.sheet, self.counter, 1, sStep, True, "white", "black")
        self.excel.setCellData(self.sheet, self.counter, 2, sDesciption, True, "white", "black")
        
        self.counter = self.counter + 1
        self.excel.saveExcel(self.book)
    

    def reportSummary(self, sReportPath):
        
        dicResult = {}
        rowCount = 3
        passedTC = 0
        failedTC = 0
        self.excel.setCellData(self.sheet, 0, 0, u"脚本通过", True, "yellow", "black", "on")
        self.excel.setCellData(self.sheet, 0, 1, u"脚本失败", True, "yellow", "black", "on")
        self.excel.setCellData(self.sheet, 2, 0, u"脚本名称", True, "yellow", "black", "on")
        self.excel.setCellData(self.sheet, 2, 1, u"运行结果", True, "yellow", "black", "on")
        self.excel.setCellData(self.sheet, 0, 2, u"")
        self.excel.setCellData(self.sheet, 0, 3, u"")
        self.excel.setCellData(self.sheet, 1, 3, u"")
        
        for report in os.listdir(sReportPath):

            if report.endswith('.xls') and not report == "report_summary.xls":
                
                excelapp = ExcelApp(sReportPath + "/" + report, [])
                book = excelapp.openExcel("r")

                sheet = excelapp.getSheetByName(book, "result")
                self.excel.setCellData(self.sheet, rowCount, 0, report.strip('.xls').strip('rpt_'))
                
                if excelapp.getCellData(sheet, 1, 3) == "Passed":   
                    self.excel.setCellData(self.sheet, rowCount, 1, excelapp.getCellData(sheet, 1, 3), True, "white", "green")
                    passedTC = passedTC + 1
                    
                elif excelapp.getCellData(sheet, 1, 3) == "Failed":
                    self.excel.setCellData(self.sheet, rowCount, 1, excelapp.getCellData(sheet, 1, 3), True, "white", "red")
                    failedTC = failedTC + 1
                    
                rowCount = rowCount + 1
         
        self.excel.setCellData(self.sheet, 1, 0, passedTC)
        self.excel.setCellData(self.sheet, 1, 1, failedTC)
        self.excel.saveExcel(self.book) 
        dicResult["PassedTS"] = passedTC
        dicResult["FailedTS"] = failedTC
        return dicResult      
            
if __name__ == '__main__':
    rpt = Reporter("report_summary.xls","summary")
    rpt.reportSummary(os.getcwd())