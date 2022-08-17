#coding:utf-8

'''
Created on May 20, 2017

@author: xiongxiaoya
'''
"""
将测试结果以HTML+附件形式发送给相关人员
"""

from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import inspect
import smtplib
from string import replace
from com.HT.SaaS.SaaSmgmt import report




def send_report():

    '''发件人'''
    from_addr = 'luozhongjian@upsoft.com.cn'
    '''收件人'''
    to_addrs = ["xiongxiaoya@upsoft.com.cn","dongchangli@upsoft.com.cn", "luozhongjian@upsoft.com.cn"]

    
    '''邮件主题'''
    message = MIMEMultipart()
    message["From"] = Header(u"测试部-自动化测试")
    message["To"] = Header("xiongxiaoya@upsoft.com.cn,dongchangli@upsoft.com.cn,luozhongjian@upsoft.com.cn")
    message["Subject"] = Header(u"审批自动化测试执行报告" )
    
    '''获取报告模板'''
#     htmlReport = open("Report_Template.txt","r").read()
    
    txtReport = "你好：\n\n【审批管理系统】 测试环境【172.16.1.59】 自动化测试结果:\n\n%s\n\n详情请查阅附件!\n\n--------------------------\
    -------------------\n自动化测试\nHT\n" % open("D:/auto_test_component/ams_log.txt", "rU").read()
    
    '''填写测试信息'''
    print open("D:/auto_test_component/ams_log.txt", "rU").read()
    message.attach(MIMEText(txtReport, "plain", "utf-8"))
    
    '''构造附件1: unittest报告'''
    att_html = MIMEApplication(open("D:/auto_test_component/automation_test_report_AMS.html", "rb").read(), "base64")
    att_html["Content-Type"] = 'application/octet-stream'
    att_html["Content-Disposition"] = 'attachment; filename="automation_test_report_AMS.html"'
    message.attach(att_html)
    
    '''构造附件2： excel报告'''
    att_excel = MIMEApplication(open("ReportSummary.xls","rb").read(),"base64")
    att_excel["Content-Type"] = 'application/octet-stream'
    att_excel["Content-Disposition"] = 'attachment; filename="AMSTestReport.xls"'
    message.attach(att_excel)
    
    '''登录邮箱服务器'''
    server = smtplib.SMTP()
    server.connect("smtp.exmail.qq.com", 25)
#     server = smtplib.SMTP_SSL("smtp.exmail.qq.com", port=465) 
    server.login("luozhongjian@upsoft.com.cn", "LZJ575700")
    
    '''发送邮件'''
    server.sendmail(from_addr, to_addrs, message.as_string())
    
    '''关闭服务器'''
    server.close()
    
    print "sent successfully"

if __name__ == '__main__':
    
    send_report()