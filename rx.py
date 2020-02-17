import serial

ser = serial.Serial('/dev/pst/7') #open serial port
print .ser.portstr
print
r=ser.readLine()
print ser.close()
