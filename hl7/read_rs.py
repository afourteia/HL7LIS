import serial
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


buffer = bytes()  # .read() returns bytes right?
print('buffer',buffer)
ser = serial.Serial("COM8")
while True:
    if ser.in_waiting > 0:
        
        # print(ser.in_waiting )
        data = ser.read(ser.in_waiting)
        # print("data is: ", (data))
        buffer += data
        # print('buffer2***************',buffer)
        if buffer == 0x1c: 
            print('start')
        try:
            # complete = buffer
            complete = buffer[:buffer.index(b'')+1]  # get up to '}'
            # print(complete)
            buffer = buffer[buffer.index(b'')+1:]  # leave the rest in buffer
        except ValueError as e:
            print(e)
            continue  # Go back and keep reading
        print('buffer=', complete)
        print('buffer=',type( complete))
        # messages = complete.partition('|')
        
        # print("messages 333333333333333333333333333",messages)
        ascii = buffer.decode('utf-8')
        # print("ASCII in Hex is: ", bytes.fromhex(ascii))
        print('utf-8=', ascii)