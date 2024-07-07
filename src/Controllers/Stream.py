import serial
import serial.tools.list_ports

from src.Utils.XMLUtils import XMLUtils

class Stream:
    """
    A class to manage serial communication via a specified port.

    Attributes
    ----------
    __port : str
        The serial port to connect to.
    __baudRate : int
        The baud rate for the serial communication.
    __timeOut : int, optional
        The timeout for the serial connection (default is 1 second).
    __SerialConnection : serial.Serial or None
        The serial connection object.

    Methods
    -------
    ChangePort(port)
        Changes the serial port and reconnects.
    ChangeBaudRate(baudRate)
        Changes the baud rate and reconnects.
    Post(content)
        Sends content through the serial connection.
    Get()
        Receives data from the serial connection.
    """

    def __init__(self, port, baudRate, timeOut=1):
        """
        Initializes the Stream with the specified port, baud rate, and timeout.

        Parameters
        ----------
        port : str
            The serial port to connect to.
        baudRate : int
            The baud rate for the serial communication.
        timeOut : int, optional
            The timeout for the serial connection (default is 1 second).
        """
        self.__port = port
        self.__baudRate = baudRate
        self.__timeOut = timeOut
        self.__SerialConnection = None
        self.__eelRef = None
        # self.Connect()
        # self.Reconnect()


    def GetPort(self):
        return self.__port
    
    def GetBaudRate(self):
        return self.__baudRate
    

    def SetEel(self, eelRef):
        self.__eelRef = eelRef
    
    def SetPort(self, port):
        self.__port = port

    def SetBaudRate(self, baudRate):
        self.__baudRate = baudRate

    def LogSerialData(self):
        while self.__SerialConnection.is_open:
            data = self.Get()
            if data:
                self.__eelRef.UpdateLogWindow(data)()

    def Connect(self):
        """
        Establishes the serial connection with the specified port, baud rate, and timeout.

        Raises
        ------
        serial.SerialException
            If the connection attempt fails.
        """
        try:
            self.__SerialConnection = serial.Serial(
                port=self.__port, 
                baudrate=self.__baudRate, 
                timeout=self.__timeOut
            )
            print(f'Connected on port: {self.__port} with baudrate: {self.__baudRate}')
            return f'Connected on port: {self.__port} with baudrate: {self.__baudRate}'
        except serial.SerialException as e:
            print(f'Connection unsuccessful on port: {self.__port} with baudrate: {self.__baudRate}')
            return f'Connection unsuccessful on port: {self.__port} with baudrate: {self.__baudRate}'

    def Reconnect(self):
        """
        Reconnects the serial connection by closing it if open and then re-establishing it.
        """
        if self.__SerialConnection and self.__SerialConnection.is_open:
            self.__SerialConnection.close()
        self.Connect()

    def ChangePort(self, port):
        """
        Changes the serial port and reconnects.

        Parameters
        ----------
        port : str
            The new serial port to connect to.
        """
        self.__port = port
        self.__SerialConnection.port = port
        self.Reconnect()

    def ChangeBaudRate(self, baudRate):
        """
        Changes the baud rate and reconnects.

        Parameters
        ----------
        baudRate : int
            The new baud rate for the serial communication.
        """
        self.__baudRate = baudRate
        self.__SerialConnection.baudrate = baudRate
        self.Reconnect()

    @staticmethod
    def ListComPorts():
        ports = serial.tools.list_ports.comports()
        return [{"port": port.device, "description": port.description} for port in ports]

    def Post(self, content):
        """
        Sends content through the serial connection.

        Parameters
        ----------
        content : str
            The content to send through the serial connection.
        
        Raises
        ------
        Exception
            If an error occurs during the sending of data.
        """
        try:
            self.__SerialConnection.write(content.encode('utf-8'))
        except Exception as e:
            print(f'Error in Post method: {e}')

    def Get(self):
        """
        Receives data from the serial connection.

        Returns
        -------
        str or None
            The received data as a string, or None if no data is available.
        """
        if self.__SerialConnection and self.__SerialConnection.is_open:
            if self.__SerialConnection.in_waiting:
                data = self.__SerialConnection.readline().decode('utf-8').rstrip()
                return data
        return None
