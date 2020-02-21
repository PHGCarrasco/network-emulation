import serial
ser = serial.Serial('/dev/pts/1')  # open serial port
print ser.portstr       # check which port was really used
print
r=ser.readline()        # read  a string
print r			# print the string
ser.close()             # close port

