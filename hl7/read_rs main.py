import serial
import codecs
import serial.tools.list_ports

# # ser = serial.Serial('/dev/ttyUSB0')  # open serial port
# ser = serial.Serial("COM8")
# print(ser.name)         # check which port was really used
# data = ser.read() 
# print(data)# write a string
# ser.close()             # close port

# with serial.Serial("COM8") as ser:
#      x = ser.read().decode('utf-8')         # read one byte
#      print('x',x)
#      s = ser.read(10).decode('utf-8')        # read up to ten bytes (timeout)
#      print('s',s)
def main():
    try:
        buffer = bytes()
        ports = serial.tools.list_ports.comports(include_links=False)
        if ports:
            for port in ports:
             print('Found port ' + port.device)
        ser = serial.Serial(port.device)
        # ser = serial.Serial("COM8")
        while True:
            if ser.in_waiting > 0:
                data = ser.read(ser.in_waiting)
                print("data is: ", (data))
                try:
                    buffer += data 
                    # print("utf 8",buffer.decode("utf-8"))
                except ValueError as e:
                    print(e)
                    continue  # Go back and keep reading
                print("full ******************************")
                print(buffer)
                with open('full_message.txt', 'w') as f:
                #  f.write(buffer.decode("utf-8"))
                 f.write(buffer.decode("ascii"))
                print("full end **************************8")
                output = codecs.encode(buffer, "hex")
                print("output ____________________________")
                print(output)
                # one_message = buffer.decode("utf-8").split("0b")
                # print("one !!!!!!!!!!!!!!!!!!")
                # print(one_message)
    except Exception as e:
        print(e)
main()
