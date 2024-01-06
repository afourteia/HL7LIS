import serial
import serial.tools.list_ports
from threading import Lock

# Your USB SERIAL DEVICE identification
USB_VID = "0x0403"
USB_PID = "0x6001"

SERIAL_SETTINGS = {
    "baudrate": 9600,
    "bytesize": 8,
    "parity": "N",
    "stopbits": 1,
}

LOCK = Lock()


def find_devices():
    # type: () -> List[str]
    """
    Find all COM ports corresponding to your USB device
    """
    _device_ports = []
    for port in serial.tools.list_ports.comports():
        print('port',port)
        if port.vid == int(USB_VID, 16) and port.pid == int(USB_PID, 16):
            _device_ports.append(port.device)
    return _device_ports

def read_device(device) -> str:
    # type: (str) -> str
    try:
        with LOCK:
            with serial.Serial(device_port, timeout=1, **SERIAL_SETTINGS) as ser:
                result = ser.read(size=64).decode('utf-8')
                if len(result) == 0:
                    return None
                else:
                    return result.strip("\r\n")
                return result
    except serial.SerialException as exc:
        error_message = "Cannot read serial port {}: {}".format(device_port, exc)
        print(error_message)  # or log it
        raise OSerror(error_message)


for port in find_devices():
    data = read_device(port)
    print(port)
    print(data)