
# Serial Monitor

A web-based serial monitor application for communicating with serial devices.

## Features

- Select and connect to available COM ports
- Configure baud rate for communication
- Send commands to connected devices
- Display received data in real-time

## Getting Started

### Prerequisites

- Python 3.x
- Eel library
- PySerial library

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/aleko-khomasuridze/SerialMonitor
   cd https://github.com/aleko-khomasuridze/SerialMonitor
   ```

2. Install the required Python libraries:
   ```sh
   pip install eel pyserial
   ```
   or run `setup.bat` this script will install all the required libs to run the program

### Running the Application

1. Start the application:
   ```sh
   python main.py
   ```

## Usage

1. Select the desired COM port and baud rate from the dropdown menus.
2. Click the "Connect" button to establish a connection.
3. Enter commands in the input field and click "Send" to transmit them.
4. View the sent and received data in the log window.

## Project Structure

- `main.py`: Entry point of the application.
- `src/Controllers/Stream.py`: Handles serial communication.
- `src/Utils/XMLUtils.py`: Provides XML utility functions.
- `web/`: Contains the HTML, CSS, and JavaScript files for the web interface.

## Author

Aleko Khomasuridze

## Acknowledgments

- OpenAI's ChatGPT for assistance in code documentation.
