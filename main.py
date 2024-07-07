import eel

from src.Controllers.Stream import Stream

stream:Stream = Stream("COM0", 115200)

eel.init('web')

stream.SetEel(eel)

eel.expose(Stream.ListComPorts)
eel.expose(stream.SetPort)
eel.expose(stream.SetBaudRate)
eel.expose(stream.Connect)
eel.expose(stream.LogSerialData)

if __name__ == '__main__':
    eel.start('index.html', size=(1100, 600))
