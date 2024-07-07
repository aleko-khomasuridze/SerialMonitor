
class StreamUtils {
    static port = null;
    static baudRate = null;
    static logs = [];

    static GetPort() {
        let portValue = document.getElementById('port').value;
        this.port = portValue;
        console.log(this.port);
    }

    static GetBaudRate() {
        let baudRateValue = parseInt(document.getElementById('baudRate').value);
        this.baudRate = baudRateValue;
        console.log(this.baudRate);
    }

    static UpdateComPortsList() {
        eel.ListComPorts()(function(ports) {
            let portsList = document.getElementById('port');
            portsList.innerHTML = '';
            ports.forEach(element => {
                portsList.innerHTML += `<option value="${element.port}">${element.description}</option>`;
            });
        });
    }

    static Connect() {
        this.GetPort();
        this.GetBaudRate();
        eel.SetBaudRate(this.baudRate)();
        eel.SetPort(this.port)();
        eel.Connect()(function(status) {
            if (status.startsWith("Connected")) {
                eel.LogSerialData();
            }
        });
    }

    static SendCommand() {
        let commandInput = document.getElementById('command-input');
        let command = commandInput.value;
        let logWindow = document.getElementById('log-window');
        let now = new Date();
        let dateTime = now.toLocaleTimeString();
        commandInput.value = '';
        logWindow.innerHTML += `<span style="color: #1e88e5;font-family: 'Courier New'; font-weight: bold;">[${dateTime}] -> [Sent]: </span>${command}<br>`;
        console.log(`[${dateTime}] Sent: ${command}`);
    }

    static UpdateLogWindow(data) {
        let logWindow = document.getElementById('log-window');
        let now = new Date();
        let dateTime = now.toLocaleTimeString();
        logWindow.innerHTML += `<span style="color: #1e88e5;font-family: 'Courier New'; font-weight: bold;">[${dateTime}] -> [Got]: </span>${data}<br>`;
        logWindow.scrollTop = logWindow.scrollHeight; // Scroll to the bottom
        console.log(`[${dateTime}] Got: ${data}`);
    }    
}

eel.expose(UpdateLogWindow);
function UpdateLogWindow(data){
    StreamUtils.UpdateLogWindow(data);
}

document.getElementById('command-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        StreamUtils.SendCommand();
    }
});

document.addEventListener('DOMContentLoaded', function() {
    StreamUtils.UpdateComPortsList();
});
