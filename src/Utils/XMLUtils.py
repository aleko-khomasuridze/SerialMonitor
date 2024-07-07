import xml.etree.ElementTree as ET

class XMLUtils:
    """
    A utility class for handling XML file operations.

    Attributes:
        fileName (str): The name of the XML file.
        tree (ElementTree): The parsed XML tree.
        root (Element): The root element of the XML tree.

    Methods:
        __init__(fileName: str = None): Initializes the XMLUtils instance.
        GetFileName(): Returns the name of the XML file.
        ChangeFileName(fileName: str): Changes the XML file being operated on.
        GetValueOf(tagName: str): Returns the value of the specified XML tag.
        SetValueOf(tagName: str, value: str): Sets the value of the specified XML tag and saves the file.
    """

    def __init__(self, fileName: str = None) -> None:
        """
        Initializes the XMLUtils instance with the specified XML file.

        Args:
            fileName (str): The name of the XML file to be loaded. Defaults to None.
        """
        self.__fileName = fileName
        self.__tree = ET.parse(self.__fileName)
        self.__root = self.__tree.getroot()

    def GetFileName(self) -> str:
        """
        Returns the name of the XML file.

        Returns:
            str: The name of the XML file.
        """
        return self.__fileName

    def ChangeFileName(self, fileName: str) -> None:
        """
        Changes the XML file being operated on and reloads the tree and root.

        Args:
            fileName (str): The new XML file name to be loaded.
        """
        self.__fileName = fileName
        self.__tree = ET.parse(self.__fileName)
        self.__root = self.__tree.getroot()

    def GetValueOf(self, tagName: str) -> str:
        """
        Returns the value of the specified XML tag.

        Args:
            tagName (str): The name of the tag whose value is to be retrieved.

        Returns:
            str: The value of the specified tag.
        """
        return self.__root.find(tagName).text

    def SetValueOf(self, tagName: str, value: str) -> None:
        """
        Sets the value of the specified XML tag and saves the XML file.

        Args:
            tagName (str): The name of the tag whose value is to be set.
            value (str): The new value for the specified tag.
        """
        self.__root.find(tagName).text = value
        self.__tree.write(self.__fileName)
