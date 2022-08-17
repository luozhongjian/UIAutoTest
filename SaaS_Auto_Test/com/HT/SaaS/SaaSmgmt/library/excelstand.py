# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/25 15:51
@Auth ： 罗忠建

"""

import os
import sys
import xlrd
from xlutils.copy import copy
import xlwt


class ExcelApp:

    dataDir = ""
    fileName = ""
    sheetsName = ["Sheet1"]
  
    def __init__(self, fileName, sheetsName):

        self.fileName = fileName
        self.sheetsName = sheetsName

        baseDir = sys.path[0]
        dataDir = ""
        
        if os.path.isdir(baseDir):
            dataDir = baseDir
        elif os.path.isfile(baseDir):
            dataDir = os.path.dirname(baseDir)
            
        if not os.path.isfile(fileName):            
            reportBook = xlwt.Workbook()
            for sht in self.sheetsName:
                reportBook.add_sheet(sht)
#             self.fileName = "".join([dataDir.replace("\\", "/"), "/", self.fileName])
            print(self.fileName)
            reportBook.save(self.fileName)

    # 打开Excel
    def openExcel(self, mode):
        if mode == 'w':
            return copy(xlrd.open_workbook(self.fileName))
        elif mode == 'r': 
            return xlrd.open_workbook(self.fileName)


    # 获取工作表序号
    def getSheetByIndex(self,book, sheetIndex):
        sheet = book.get_sheet(sheetIndex)
        return sheet
    

    # 获取工作表名称
    def getSheetByName(self, book, sheetName):
        sheet = book.sheet_by_name(sheetName)
        return sheet

    # 保存Excel
    def saveExcel(self, book):
        book.save(self.fileName)
#         book.close()

    # 获取所有工作表名称
    def getSheetsName(self):
        sheetlist = []
        book = xlrd.open_workbook(self.fileName)
        for sheet in book.sheets():
            sheetlist.append(sheet.name)

        return sheetlist

    # 设置单元格数据
    def setCellData(self, sheetObj, row, col, cellValue, highlight = False, backcolor= "white", fontcolor = "black", bold = "off", border = 0, font_name = 'HP Simplified'):

        borders = xlwt.Borders()
        borders.top = border
        borders.bottom = border
        borders.left = border
        borders.right = border
        
        if highlight == False:
            sheetObj.write(row, col, cellValue)
        else:
            style = xlwt.easyxf('pattern: pattern solid, fore-color ' + backcolor+'; font:color-index '+ fontcolor + ',bold ' + bold+',name ' + font_name)
            style.borders = borders
            sheetObj.write(row, col, cellValue, style)

    def setColWidth(self,sheetObj, colNo, widthSize):
        sheetObj.col(colNo).width = widthSize

    # 获取行数据
    # Mode: read
    def getRowData(self, sheetObj, row):
        return sheetObj.row_values(row)

    # 获取列数据
    # Mode: read
    def getColData(self, sheetObj, col):
        return sheetObj.col_values(col)

    # 获取单元格数据
    def getCellData(self, sheetObj, row, col):

        cellData = ""
        try:
           #data = xlrd.open_workbook(self.fileName)
            cellData = sheetObj.cell(row, col).value
        finally:
            return cellData

    # 获取行数
    def getRowCount(self,sheetName, col):
            return xlrd.open_workbook(self.fileName).sheet_by_name(sheetName).nrows
        

    # 获取列数
    def getColCount(self, sheetName, row):
        return xlrd.open_workbook(self.fileName).sheet_by_name(sheetName).ncols
    

    # 获取合并单元格的列数
    def mergeCells(self, sheetObj, iTopRowNo, iBottomRowNo, iLeftColNo, iRightColNo):
        sheetObj.merge(iTopRowNo, iBottomRowNo, iLeftColNo, iRightColNo)


if __name__=="__main__":

    excel = ExcelApp(r"C:\Users\admin\Desktop\122.xls", ["Sheet1"])
    book = excel.openExcel("w")
    sheet = excel.getSheetByIndex(book, 0)
    excel.setCellData(sheet, 0, 0, "Test",True, "blue")
    excel.mergeCells(sheet, 0, 0, 0, 2)
    excel.saveExcel(book)
    
#     book = excel2.openExcel('r')
#     print excel2.getCellData(excel2.getSheetByName(book,"Sheet 1"), 0, 0)
#     excel = ExcelApp("C:\Users\admin\Desktop\122.xls",["Compare Result"])
#     aBook = excel.openExcel('w')
#     aSheet = excel.getSheetByIndex(aBook, 0)
#     print "***"+excel.getCellData(aSheet, 0, 0)
#     excel.setCellData(aSheet,2, 4, "sssss")
#     excel.saveExcel(aBook)
#     excel.setCellData(0, 1, 1, "test", True)
        