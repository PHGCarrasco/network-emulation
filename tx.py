import serial
ser = serial.Serial('/dev/pts/0')  # open first serial port
print ser.portstr       # check which port was really used
ser.write('Ola Mundo\n')  # write a string
ser.close()             # close port
