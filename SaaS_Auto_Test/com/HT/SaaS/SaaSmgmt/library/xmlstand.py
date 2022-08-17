# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/25 15:59
@Auth ： 罗忠建

"""
import time
import xml.etree.ElementTree as ET

class XmlApp:
    '''
    classdocs
    '''
    fileName = ""
    rootNode = ""

    def __init__(self, fileName):

        self.fileName = fileName
        try:
            tree = ET.parse(self.fileName)
            self.rootNode = tree.getroot()
        except:
            print("打开文件失败!")

    #获取标签和属性
    def getNodeText(self, parentNode, childNode):
        dicNodeValue = {}
        try:
            for nd in self.rootNode.iter(parentNode):
                print()
                dicNodeValue[childNode]= nd.find(childNode).text
            return dicNodeValue
        except:
            return {'提示':'获取失败'}

    #获取所有子标签
    def getNodesTextbyParentName(self,parentNodeName):

        textList = []
        for t in self.rootNode.findall(".//" + parentNodeName + "/*"):
            textList.append(t.tag)
        return textList

    #获取标签下的属性
    def getNodesByTag(self, childNodeTag):

        return self.rootNode.findall(".//" + childNodeTag)


if __name__ == "__main__":
    pass
    # xmlApp = XmlApp("access.xml")
    # # print(xmlApp.getNodeText("BP", "addr"))
    # # print(xmlApp.getNodesTextbyParentName("BP"))
    # # print(xmlApp.getNodesByTag("addr")[0].text)
    # # print(xmlApp.getNodesByTag("username")[0].text)
    # print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+".log")


