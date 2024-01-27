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
HEADER ='0b'
TRAILER = '1c0d'

def main():
    try:
        buffer = bytes()
        ports = serial.tools.list_ports.comports(include_links=False)
        if ports:
            for port in ports:
             print('Found port ' + port.device)
        # ser = serial.Serial(port.device)
        ser = serial.Serial("COM7")
        while True:
            if ser.in_waiting > 0:
                data = ser.read(ser.in_waiting)
                print("data is: ", (data) ,end='\n')
                try:
                    buffer += data 
                    # print("utf 8",buffer.decode("utf-8"))
                except ValueError as e:
                    print(e)
                    continue  # Go back and keep reading
                print("full ******************************" ,end='\n')
                print(buffer)
                with open('full_message.txt', 'w') as f:
                #  f.write(buffer.decode("utf-8"))
                 f.write(buffer.decode("ascii"))
                print("full end **************************8" ,end='\n')
                output = codecs.encode(buffer, "hex")
                print("output ____________________________" ,end='\n')
                print(output)
                msg = buffer.decode("utf-8")
                onemsg = msg.split(HEADER)[1]
                onemsg =onemsg.split(TRAILER)[0]
                # msg_str = buffer.decode("utf-8")str.replace(HEADER, '').replace(TRAILER, '')
                print("one !!!!!!!!!!!!!!!!!!")
                response_as_bytes = str.encode(onemsg)
                print(type(response_as_bytes))
                ser.write(response_as_bytes)
                print(onemsg)
    except Exception as e:
        print(e)
main()

