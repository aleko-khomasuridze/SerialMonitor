class StreamUtils {
    /**
     * A utility class for handling serial port communications and logging.
     */

    static port = null;
    static baudRate = null;
    static logs = [];

    /**
     * Retrieves the selected port from the dropdown and updates the class attribute.
     */
    static GetPort() {
        let portValue = document.getElementById('port').value;
        this.port = portValue;
        console.log(this.port);
    }

    /**
     * Retrieves the selected baud rate from the dropdown, converts it to an integer, and updates the class attribute.
     */
    static GetBaudRate() {
        let baudRateValue = parseInt(document.getElementById('baudRate').value);
        this.baudRate = baudRateValue;
        console.log(this.baudRate);
    }

    /**
     * Updates the list of available COM ports in the dropdown by fetching them via eel.
     */
    static UpdateComPortsList() {
        eel.ListComPorts()(function(ports) {
            let portsList = document.getElementById('port');
            portsList.innerHTML = '';
            ports.forEach(element => {
                portsList.innerHTML += `<option value="${element.port}">${element.description}</option>`;
            });
        });
    }

    /**
     * Connects to the selected port and baud rate, and starts logging serial data if connection is successful.
     */
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

    /**
     * Sends a command entered in the input field, logs the command in the log window, and clears the input field.
     */
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

    /**
     * Updates the log window with received data and scrolls to the bottom of the log window.
     * @param {string} data - The data received to be logged.
     */
    static UpdateLogWindow(data) {
        let logWindow = document.getElementById('log-window');
        let now = new Date();
        let dateTime = now.toLocaleTimeString();
        logWindow.innerHTML += `<span style="color: #1e88e5;font-family: 'Courier New'; font-weight: bold;">[${dateTime}] -> [Got]: </span>${data}<br>`;
        logWindow.scrollTop = logWindow.scrollHeight; // Scroll to the bottom
        console.log(`[${dateTime}] Got: ${data}`);
    }
}

// Expose the UpdateLogWindow method to eel
eel.expose(UpdateLogWindow);

/**
 * Updates the log window with the received data by calling the StreamUtils method.
 * @param {string} data - The data received to be logged.
 */
function UpdateLogWindow(data) {
    StreamUtils.UpdateLogWindow(data);
}

// Add an event listener to send a command when Enter key is pressed in the command input field
document.getElementById('command-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        StreamUtils.SendCommand();
    }
});

// Initialize the COM ports list when the document content is loaded
document.addEventListener('DOMContentLoaded', function() {
    StreamUtils.UpdateComPortsList();
});
