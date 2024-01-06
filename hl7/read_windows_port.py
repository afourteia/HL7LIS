import serial

# ser = serial.Serial("COM8", baudrate=9600, timeout=None)
ser = serial.Serial("COM8")
mgs= ""
while True:
   data = ser.read()
   if data != "":
      mgs += data.decode('utf-8')
   print(data)
   print(mgs)

# while True:
#    bytesToRead = ser.inWaiting()
#    data = ser.read(bytesToRead)
#    print(data)


# from serial.tools import list_ports
# port = list(list_ports.comports())
# all = list_ports
# print(all)
# for p in port:
#     print(p.device)


