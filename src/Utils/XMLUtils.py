import xml.etree.ElementTree as ET

class XMLUtils:
    def __init__(self, fileName:str = None) -> None:
        self.__fileName = fileName
        self.__tree = ET.parse(self.__fileName)
        self.__root = self.__tree.getroot()

    def GetFileName(self):
        return self.__fileName

    
    def ChangeFileName(self, fileName):
        self.__fileName = fileName
        self.__tree = ET.parse() 
        self.__root = self.__tree.getroot()


    def GetValueOf(self, tagName:str):
        return self.__root.find(tagName).text
    
    def SetValueOf(self, tagName:str, value:str):
        self.__root.find(tagName).text = value
        self.__tree.write(self.__fileName)