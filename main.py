import eel
from src.Controllers.Stream import Stream

# Initialize the Stream object with a default port and baud rate
stream = Stream("COM0", 115200)

# Initialize the eel web folder
eel.init('web')

# Set eel instance to the stream object for communication
stream.SetEel(eel)

# Expose Stream class methods to JavaScript
eel.expose(Stream.ListComPorts)  # Expose the method to list COM ports
eel.expose(stream.SetPort)       # Expose the method to set the COM port
eel.expose(stream.SetBaudRate)   # Expose the method to set the baud rate
eel.expose(stream.Connect)       # Expose the method to connect to the serial port
eel.expose(stream.LogSerialData) # Expose the method to log serial data

if __name__ == '__main__':
    # Start the eel application with the specified HTML file and window size
    eel.start('index.html', size=(1100, 600))
